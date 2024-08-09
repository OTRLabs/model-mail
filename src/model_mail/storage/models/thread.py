from __future__ import annotations

from typing import List, Optional
from rich.console import Console
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, relationship, backref
from dataclasses import dataclass
from advanced_alchemy.base import UUIDAuditBase 
from advanced_alchemy.exceptions import IntegrityError
from __future__ import annotations

from typing import TYPE_CHECKING

from litestar import Litestar
from litestar.controller import Controller
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import delete, get, patch, post
from litestar.params import Parameter
from pydantic import BaseModel as _BaseModel
from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload

from advanced_alchemy.base import UUIDAuditBase, UUIDBase
from advanced_alchemy.extensions.litestar import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyPlugin,
    async_autocommit_before_send_handler,
)
from advanced_alchemy.filters import FilterTypes, LimitOffset
from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import OffsetPagination, SQLAlchemyAsyncRepositoryService



if TYPE_CHECKING:
    from collections.abc import AsyncGenerator
    from datetime import date
    from uuid import UUID

    from sqlalchemy.ext.asyncio import AsyncSession





class Thread(UUIDAuditBase):
    __tablename__ = "threads"

    id: Mapped[int]
    subject: Mapped[str]
    folder_id: Mapped[int]

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