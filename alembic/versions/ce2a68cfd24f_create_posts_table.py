"""create posts table

Revision ID: ce2a68cfd24f
Revises: 
Create Date: 2024-03-21 18:29:57.918500

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ce2a68cfd24f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
