"""empty message

Revision ID: 0a673209e20c
Revises: 568df317f17b
Create Date: 2024-07-19 09:52:10.520601

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer

# revision identifiers, used by Alembic.
revision = '0a673209e20c'
down_revision = '568df317f17b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table("users")


def downgrade() -> None:
    pass
