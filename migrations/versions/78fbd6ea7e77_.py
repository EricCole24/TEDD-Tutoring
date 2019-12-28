"""empty message

Revision ID: 78fbd6ea7e77
Revises: 
Create Date: 2019-12-25 07:37:48.396559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78fbd6ea7e77'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('studentsignup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Firstname', sa.String(length=120), nullable=True),
    sa.Column('Lastname', sa.String(length=120), nullable=True),
    sa.Column('Email', sa.String(length=120), nullable=True),
    sa.Column('Password', sa.String(length=120), nullable=True),
    sa.Column('Contact', sa.Integer(), nullable=True),
    sa.Column('School', sa.String(length=120), nullable=True),
    sa.Column('Classification', sa.String(length=120), nullable=True),
    sa.Column('Major', sa.String(length=120), nullable=True),
    sa.Column('Gender', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('Email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('studentsignup')
    # ### end Alembic commands ###