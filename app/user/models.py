from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from app.models import DefaultBase


class User(DefaultBase):
    __tablename__ = 'User'

    email: Mapped[str] = mapped_column(nullable=False, unique=True , index=True)
    password: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    date_of_birth: Mapped[date] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(nullable=False)