from sqlalchemy.orm import Session

from .models import User, Record


def create_db_user(db: Session, username: str) -> User:
    """
    Saves and returns a single user object.
    """
    new_user: User = User(name=username)
    db.add(new_user)
    db.commit()

    return new_user


def get_db_user(db: Session, id: int) -> User:
    """
    Returns a single user object from the db.
    """
    user: User = db.query(User).get(id)

    return user


def insert_db_audio(db: Session, filename: str, record: str, user_id: int) -> Record:
    """
    Saves and returns a single record object.
    """
    new_record: Record = Record(filename=filename, record=record, user_id=user_id)
    db.add(new_record)
    db.commit()

    return new_record


def get_db_audio(db: Session, id: str) -> Record:
    """
    Returns a single record object from the db.
    """
    record: Record = db.query(Record).get(id)

    return record
