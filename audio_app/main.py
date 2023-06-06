from typing import Annotated

from fastapi import FastAPI, Depends, UploadFile, File, Form, Request, Response
from sqlalchemy.orm import Session
from starlette.responses import FileResponse, JSONResponse

from audio_app import models
from audio_app.crud import create_db_user, insert_db_audio, get_db_user, get_db_audio
from audio_app.db import engine
from audio_app.models import User, Record
from audio_app.schemas import UserOutput, UserCreate, UploadOutput
from audio_app.utils import process_wav_file, process_filename
from audio_app.db import SessionLocal

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db() -> Session:
    with SessionLocal() as session:
        yield session


@app.post('/user/create/', response_model=UserOutput)
def create_user(username: UserCreate, db: Session = Depends(get_db)):
    username: str = username.username
    if not all([username, username.isalpha(), 8 <= len(username) <= 100]):
        return JSONResponse(status_code=422,
                            content={
                                'message': '"Username" must be 8 to 100 characters long and contain only letters'
                            })
    new_user: User = create_db_user(db, username)

    return {'credentials': {'id': new_user.id, 'token': new_user.token}}


@app.post('/record/', response_model=UploadOutput)
def add_audio(user_id: Annotated[int, Form()], user_token: Annotated[str, Form()],
              wav_file: Annotated[UploadFile, File()], request: Request, db: Session = Depends(get_db)):
    user: User = get_db_user(db, user_id)

    if not (user and user_token == str(user.token)):
        return JSONResponse(status_code=401,
                            content={
                                'message': "User with the given ID and token doesn't exist"
                            })

    if not wav_file.filename.endswith('.wav'):
        return JSONResponse(status_code=422,
                            content={
                                'message': 'Make sure your file contains a name and a "wav" extension - "example.wav"'
                            })

    filename: str = process_filename(wav_file)
    mp3_form_bytes: str = process_wav_file(wav_file)
    new_record: Record = insert_db_audio(db, filename, mp3_form_bytes, user_id)

    return {
        'result': {
            'link to record': str(request.url_for('get_audio')) + f'?id={new_record.id}&user={new_record.user_id}'
        }}


@app.get('/record/', response_class=FileResponse)
def get_audio(id: str, user: int, db: Session = Depends(get_db)):
    if len(id) != 36:
        return JSONResponse(status_code=422,
                            content={
                                'message': '"ID" must be 36 characters long'
                            })

    record: Record = get_db_audio(db, id)

    if not (record and record.user_id == user):
        return JSONResponse(status_code=404,
                            content={
                                'message': "Record with the given ID and token hasn't been found"
                            })

    file: bytes = record.record
    headers: dict = {'Content-Disposition': f'attachment; filename="{record.filename}"'}

    return Response(file, headers=headers, media_type='audio/mp3')
