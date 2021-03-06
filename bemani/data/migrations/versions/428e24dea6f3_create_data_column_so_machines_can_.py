"""Create data column so machines can include extra settings.

Revision ID: 428e24dea6f3
Revises: 23a589a1785c
Create Date: 2017-12-18 22:43:42.133159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '428e24dea6f3'
down_revision = '23a589a1785c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('machine', sa.Column('data', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('machine', 'data')
    # ### end Alembic commands ###
