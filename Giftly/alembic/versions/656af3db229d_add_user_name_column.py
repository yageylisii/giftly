"""Add user_name column

Revision ID: 656af3db229d
Revises: c28705410e2f
Create Date: 2025-06-16 20:18:25.154341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '656af3db229d'
down_revision: Union[str, None] = 'c28705410e2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('user_name', sa.String(), nullable=False, server_default='0'))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'user_name')
    # ### end Alembic commands ###
