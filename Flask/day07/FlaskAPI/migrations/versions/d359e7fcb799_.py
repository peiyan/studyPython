"""empty message

Revision ID: d359e7fcb799
Revises: 1948453527e9
Create Date: 2018-08-07 11:55:20.783614

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd359e7fcb799'
down_revision = '1948453527e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('axf_wheel',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('img', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('trackid', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('wheel')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wheel',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('img', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('trackid', mysql.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('axf_wheel')
    # ### end Alembic commands ###