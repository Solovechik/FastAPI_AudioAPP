import uuid

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str


class UserCredentials(BaseModel):
    id: int
    token: uuid.UUID


class UserOutput(BaseModel):
    credentials: UserCredentials


class UploadOutput(BaseModel):
    result: dict[str, str]
