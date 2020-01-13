"""empty message

Revision ID: 517c1cfbc3af
Revises: 194befb66d6f
Create Date: 2020-01-06 02:43:49.306725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '517c1cfbc3af'
down_revision = '194befb66d6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('schedulesignup', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_schedulesignup_timestamp'), 'schedulesignup', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_schedulesignup_timestamp'), table_name='schedulesignup')
    op.drop_column('schedulesignup', 'timestamp')
    # ### end Alembic commands ###