"""add allow_text_parameters column

Revision ID: a1b2c3d4e5f6
Revises: e9fb734d8566
Create Date: 2025-11-11 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a1b2c3d4e5f6"
down_revision = "e9fb734d8566"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("dashboards", sa.Column("allow_text_parameters", sa.Boolean(), nullable=True, server_default=sa.false()))


def downgrade():
    op.drop_column("dashboards", "allow_text_parameters")
