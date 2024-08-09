from __future__ import annotations

from typing import List, Optional
from rich.console import Console
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, relationship, backref

from advanced_alchemy import dataclass, UUIDAuditBase


@dataclass
class Thread:
    __tablename__ = "threads"

    id: int
    subject: str
    folder_id: int

    def save(self, session: Session) -> None:
        session.add(self)
        session.commit()

    @classmethod
    def get_by_id(cls, session: Session, thread_id: int) -> Optional[Thread]:
        return session.query(cls).filter(cls.id == thread_id).first()

    @classmethod
    def get_by_subject(cls, session: Session, subject: str) -> Optional[Thread]:
        return session.query(cls).filter(cls.subject == subject).first()

    @classmethod
    def get_by_folder_id(cls, session: Session, folder_id: int) -> List[Thread]:
        return session.query(cls).filter(cls.folder_id == folder_id).all()