"""add content column to post table

Revision ID: 4f879183fc4a
Revises: 0be6e83d6c99
Create Date: 2022-01-15 15:01:16.513859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f879183fc4a'
down_revision = '0be6e83d6c99'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
