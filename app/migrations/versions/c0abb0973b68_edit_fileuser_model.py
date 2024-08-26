"""Edit FileUser model

Revision ID: c0abb0973b68
Revises: d0c1790c34ee
Create Date: 2024-08-26 14:23:25.364687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0abb0973b68'
down_revision: Union[str, None] = 'd0c1790c34ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('FileUser', sa.Column('format', sa.String(), nullable=False))
    op.drop_constraint('comment_user_uc', 'FileUser', type_='unique')
    op.create_unique_constraint('name_format_user_uc', 'FileUser', ['name', 'format', 'author_id'])
    op.drop_column('FileUser', 'type')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('FileUser', sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint('name_format_user_uc', 'FileUser', type_='unique')
    op.create_unique_constraint('comment_user_uc', 'FileUser', ['name', 'type', 'author_id'])
    op.drop_column('FileUser', 'format')
    # ### end Alembic commands ###
