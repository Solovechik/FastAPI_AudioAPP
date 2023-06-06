import uuid

from sqlalchemy import Column, Integer, String, UUID, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship

from audio_app.db import Base


class User(Base):
    __tablename__ = 'audio_users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    token = Column(UUID(as_uuid=True), default=uuid.uuid4)
    records = relationship('Record', back_populates='user')

    def __init__(self, name):
        self.name = name


class Record(Base):
    __tablename__ = 'audio_records'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = Column(String(150), nullable=False)
    record = Column(LargeBinary, nullable=False)
    user_id = Column(Integer, ForeignKey('audio_users.id'))
    user = relationship('User', back_populates='records')

    def __init__(self, filename, record, user_id):
        self.filename = filename
        self.record = record
        self.user_id = user_id
