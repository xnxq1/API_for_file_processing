from sqlalchemy import ForeignKey

from app.models import DefaultBase
from sqlalchemy.orm import Mapped, mapped_column

class FileUser(DefaultBase):
    __tablename__ = 'FileUser'
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    author_id: Mapped[int] = mapped_column(ForeignKey('User.id'))