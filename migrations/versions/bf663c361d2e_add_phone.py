"""add phone

Revision ID: bf663c361d2e
Revises: 3af008ed4f58
Create Date: 2023-08-14 09:02:08.919498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf663c361d2e'
down_revision = '3af008ed4f58'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('complaints', 'photo_url',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('complaints', 'photo_url',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    # ### end Alembic commands ###