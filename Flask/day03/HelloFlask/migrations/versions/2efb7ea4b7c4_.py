"""empty message

Revision ID: 2efb7ea4b7c4
Revises: 1dbbe4d73024
Create Date: 2018-08-01 17:13:41.203736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2efb7ea4b7c4'
down_revision = '1dbbe4d73024'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('s_age', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 's_age')
    # ### end Alembic commands ###
