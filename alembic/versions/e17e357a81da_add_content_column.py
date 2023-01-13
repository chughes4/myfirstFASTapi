"""add content column

Revision ID: e17e357a81da
Revises: 92d47ba61fcd
Create Date: 2023-01-10 01:15:58.298759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e17e357a81da'
down_revision = '92d47ba61fcd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
