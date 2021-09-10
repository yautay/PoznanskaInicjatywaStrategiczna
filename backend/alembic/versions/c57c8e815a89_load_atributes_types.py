"""load_atributes_types

Revision ID: c57c8e815a89
Revises: 
Create Date: 2021-09-10 20:40:18.857194

"""
from alembic import op
import sqlalchemy as sa
from db.models.data.data_bgg_game_attributes_types import DataBggGameAttributesTypes as at
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

# revision identifiers, used by Alembic.
revision = 'c57c8e815a89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create an ad-hoc table to use for the insert statement.
    bgg_game_attributes_types = table('bgggameattributestypes',
                                      column('attribute_type_index', Integer),
                                      column('attribute_type_name', String)
                                      )
    op.bulk_insert(bgg_game_attributes_types, at.data())


def downgrade():
    op.execute("DELETE FROM bgggameattributestypes")
