"""empty message

Revision ID: 1472c09a5f30
Revises: 7563948b916c
Create Date: 2020-01-05 05:55:00.574985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1472c09a5f30'
down_revision = '7563948b916c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('studentsignup', sa.Column('Firstname', sa.String(length=120), nullable=True))
    op.drop_column('studentsignup', 'Contact')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('studentsignup', sa.Column('Contact', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('studentsignup', 'Firstname')
    # ### end Alembic commands ###
