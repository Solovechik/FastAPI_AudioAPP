import uuid

from sqlalchemy import Integer, String, UUID, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from audio_app.db import Base


class User(Base):
    __tablename__ = 'audio_users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    token: Mapped[UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4)
    records: Mapped[list["Record"]] = relationship('Record', back_populates='user')


class Record(Base):
    __tablename__ = 'audio_records'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename: Mapped[str] = mapped_column(String(150), nullable=False)
    record: Mapped[str] = mapped_column(LargeBinary, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('audio_users.id'))
    user: Mapped["User"] = relationship('User', back_populates='records')
