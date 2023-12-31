"""empty message

Revision ID: ec7af82bfb6f
Revises: 0b7394bbaf85
Create Date: 2023-09-20 20:14:18.174479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec7af82bfb6f'
down_revision = '0b7394bbaf85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cities')
    op.drop_table('countries')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('countries',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('countries_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='countries_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('cities',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('country_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('visited', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['countries.id'], name='cities_country_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='cities_pkey')
    )
    # ### end Alembic commands ###
