"""empty message

Revision ID: 8e3bf384a45
Revises: None
Create Date: 2014-06-08 22:06:31.574747

"""

# revision identifiers, used by Alembic.
revision = '8e3bf384a45'
down_revision = None

from alembic import op
from sqlalchemy import INTEGER, VARCHAR, Column


def upgrade():
    op.create_table('assets',
                    Column('asset_id', INTEGER, primary_key=True),
                    Column('state_id', INTEGER),
                    Column('type_id', INTEGER))

    op.create_table('attributes',
                    Column('id', INTEGER, primary_key=True),
                    Column('name', VARCHAR(50), nullable=False))

    op.create_table('resources',
                    Column('id', INTEGER, primary_key=True),
                    Column('name', VARCHAR(50), nullable=False))

    op.create_table('states',
                    Column('id', INTEGER, primary_key=True),
                    Column('name', VARCHAR(20), nullable=False))

    op.create_table('tags',
                   Column('id', INTEGER, primary_key=True),
                   Column('name', VARCHAR(50), nullable=False))

    op.create_foreign_key('fk_asset_state', 'assets', 'states',
                         ['state_id'], ['id'])

    op.create_foreign_key('fk_asset_type', 'assets', 'tags',
                         ['type_id'], ['id'])


def downgrade():
    op.drop_table('attributes')
    op.drop_table('resources')
    op.drop_table('states')
    op.drop_table('tags')
