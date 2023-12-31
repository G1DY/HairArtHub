"""empty message

Revision ID: 979cc6f205c3
Revises: 
Create Date: 2023-12-28 13:34:45.273933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '979cc6f205c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=True))
        batch_op.drop_column('details')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('details', sa.INTEGER(), nullable=True))
        batch_op.drop_column('price')

    # ### end Alembic commands ###
