"""Edit FileUser model

Revision ID: d0c1790c34ee
Revises: 0d5b7544ec02
Create Date: 2024-08-26 13:54:35.082073

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0c1790c34ee'
down_revision: Union[str, None] = '0d5b7544ec02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('comment_user_uc', 'FileUser', ['name', 'type', 'author_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comment_user_uc', 'FileUser', type_='unique')
    # ### end Alembic commands ###
