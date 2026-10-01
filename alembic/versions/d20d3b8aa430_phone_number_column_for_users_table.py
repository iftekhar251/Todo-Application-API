"""phone number column for users table

Revision ID: d20d3b8aa430
Revises: 
Create Date: 2026-09-30 22:33:20.152276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd20d3b8aa430'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column('phone_number', sa.String(20), nullable=True)
    )

def downgrade() -> None:
    """Downgrade schema."""
    pass
