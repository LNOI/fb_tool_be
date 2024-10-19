"""update table

Revision ID: 241316ea6f9d
Revises: d784068639be
Create Date: 2024-10-14 13:47:47.613355

"""

from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "241316ea6f9d"
down_revision: Union[str, None] = "d784068639be"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("scopes", sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "scopes")
    # ### end Alembic commands ###
