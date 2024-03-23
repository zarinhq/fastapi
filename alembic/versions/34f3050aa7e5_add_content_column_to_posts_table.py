"""add content column to posts table

Revision ID: 34f3050aa7e5
Revises: ce2a68cfd24f
Create Date: 2024-03-22 15:43:12.235258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '34f3050aa7e5'
down_revision: Union[str, None] = 'ce2a68cfd24f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
