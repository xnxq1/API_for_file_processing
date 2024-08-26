"""Edit file model

Revision ID: 9641a389e846
Revises: f0324defe5d8
Create Date: 2024-08-25 01:57:32.787886

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9641a389e846'
down_revision: Union[str, None] = 'f0324defe5d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('FileUser_name_key', 'FileUser', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('FileUser_name_key', 'FileUser', ['name'])
    # ### end Alembic commands ###
