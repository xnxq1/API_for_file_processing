from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, declared_attr, registry



class Base(DeclarativeBase):
    pass


class DefaultBase(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)