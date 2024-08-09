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
from enum import Enum
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
    
    user_name: Mapped[str]
    email: Mapped[str]
    password_hash: Mapped[str] 
    
    
    
    
    
    
    
    
    
     