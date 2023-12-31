"""empty message

Revision ID: a45a437b775d
Revises: 4a20b5c28a45
Create Date: 2023-09-24 14:13:48.814744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a45a437b775d'
down_revision = '4a20b5c28a45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('countries', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('countries', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
