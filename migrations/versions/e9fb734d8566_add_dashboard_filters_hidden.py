"""add dashboard_filters_hidden column

Revision ID: e9fb734d8566
Revises: db0aca1ebd32
Create Date: 2025-10-27 08:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e9fb734d8566"
down_revision = "db0aca1ebd32"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("dashboards", sa.Column("dashboard_filters_hidden", sa.Boolean(), nullable=True, server_default=sa.false()))


def downgrade():
    op.drop_column("dashboards", "dashboard_filters_hidden")
