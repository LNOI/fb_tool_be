"""init table

Revision ID: 22af437c0393
Revises: 7fc2d6cf330c
Create Date: 2024-11-30 13:43:01.624781

"""

from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "22af437c0393"
down_revision: Union[str, None] = "7fc2d6cf330c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users", "emailVerified", existing_type=postgresql.TIMESTAMP(), nullable=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users", "emailVerified", existing_type=postgresql.TIMESTAMP(), nullable=False
    )
    # ### end Alembic commands ###