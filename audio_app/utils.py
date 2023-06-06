from typing import Annotated

from fastapi import UploadFile, File
from pydub import AudioSegment


def process_wav_file(wav_file: Annotated[UploadFile, File()]) -> str:
    """
    Accepts wav file from the body, converts wav to mp3, returns bytes-form of the file.
    """
    wav_file: AudioSegment = AudioSegment.from_wav(file=wav_file.file)
    mp3_form_bytes: str = wav_file.export(format='mp3').read()

    return mp3_form_bytes


def process_filename(wav_file: Annotated[UploadFile, File()]) -> str:
    """
    Accepts wav file from the body, and returns its name.
    """
    filename: str = ''.join(wav_file.filename.rsplit('.wav', 1)[:-1]) + '.mp3'

    return filename
