"""empty message

Revision ID: febc4ed44f31
Revises: 6bf71540a8a6
Create Date: 2019-12-31 03:18:38.648421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'febc4ed44f31'
down_revision = '6bf71540a8a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Preferedname', sa.String(length=120), nullable=True),
    sa.Column('Classes', sa.String(length=120), nullable=True),
    sa.Column('Taken', sa.String(length=120), nullable=True),
    sa.Column('Areas', sa.String(length=120), nullable=True),
    sa.Column('Comment', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_data')
    # ### end Alembic commands ###
