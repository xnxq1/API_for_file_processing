from sqlalchemy import ForeignKey, UniqueConstraint

from app.models import DefaultBase
from sqlalchemy.orm import Mapped, mapped_column

class FileUser(DefaultBase):
    __tablename__ = 'FileUser'
    name: Mapped[str] = mapped_column(nullable=False)
    format: Mapped[str] = mapped_column(nullable=False)
    size: Mapped[int] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey('User.id'))
    is_download: Mapped[bool] = mapped_column(nullable=False)

    __table_args__ = (
        UniqueConstraint('name', 'format', 'author_id', name='name_format_user_uc'),
    )