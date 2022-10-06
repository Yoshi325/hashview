"""empty message

Revision ID: 041d9052ff2a
Revises: 93ee907daf68
Create Date: 2022-10-06 21:31:49.437896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '041d9052ff2a'
down_revision = '93ee907daf68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('queued_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('jobs', 'queued_at')
    # ### end Alembic commands ###
