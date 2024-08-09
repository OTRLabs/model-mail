from __future__ import annotations

from typing import TYPE_CHECKING
from typing import List 

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
from enum import Enum

import asyncio

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator
    from datetime import date
    from uuid import UUID

    from sqlalchemy.ext.asyncio import AsyncSession


class UserRoles(str, Enum):
    ADMIN: str = "admin"
    MANAGER: str = "manager"
    CUSTOMER: str = "customer"
    

class CustomerTier(str, Enum):
    GOLD: str = "gold"
    SILVER: str = "silver"
    BRONZE: str = "bronze"
    FREE: str = "free"

class User(UUIDBase):
    
    __table__ = "users"
    
    user_name: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    
    password_hash: Mapped[str] = mapped_column(nullable=False)
    
    
    role: Mapped[UserRoles] = mapped_column(nullable=False)
    
    if role == UserRoles.CUSTOMER:
        tier: Mapped[CustomerTier] = mapped_column(nullable=False)
        
    
    async def save(self, session: AsyncSession) -> None:
        session.add(self)
        await session.commit()
        
     
    
    
    
    
    
    
    
    
    
     