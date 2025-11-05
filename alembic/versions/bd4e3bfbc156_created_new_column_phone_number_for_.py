"""created new column 'phone_number' for users table

Revision ID: bd4e3bfbc156
Revises: 
Create Date: 2025-11-04 23:28:45.327744

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd4e3bfbc156'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')
