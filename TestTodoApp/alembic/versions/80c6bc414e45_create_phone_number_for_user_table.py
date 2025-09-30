"""Create phone number for User table

Revision ID: 80c6bc414e45
Revises: 
Create Date: 2025-09-04 09:55:26.017904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80c6bc414e45'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(length=10), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    pass
