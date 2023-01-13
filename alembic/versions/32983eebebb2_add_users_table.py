"""add users table

Revision ID: 32983eebebb2
Revises: e17e357a81da
Create Date: 2023-01-10 01:30:55.632869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32983eebebb2'
down_revision = 'e17e357a81da'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
