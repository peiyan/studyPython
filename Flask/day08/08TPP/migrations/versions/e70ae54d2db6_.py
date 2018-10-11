"""empty message

Revision ID: e70ae54d2db6
Revises: 0467f2f2922e
Create Date: 2018-08-08 15:56:18.036388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e70ae54d2db6'
down_revision = '0467f2f2922e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('icon', sa.String(length=30), nullable=True),
    sa.Column('token', sa.String(length=255), nullable=True),
    sa.Column('permission', sa.Integer(), nullable=True),
    sa.Column('isactive', sa.Boolean(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
