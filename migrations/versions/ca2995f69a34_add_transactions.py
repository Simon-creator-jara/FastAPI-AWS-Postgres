"""add transactions

Revision ID: ca2995f69a34
Revises: bf663c361d2e
Create Date: 2023-08-14 14:40:30.749039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca2995f69a34'
down_revision = 'bf663c361d2e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quote_id', sa.String(length=120), nullable=False),
    sa.Column('transfer_id', sa.Integer(), nullable=False),
    sa.Column('target_account_id', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('complaint_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['complaint_id'], ['complaints.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    # ### end Alembic commands ###
