"""update table

Revision ID: e611c6511870
Revises: 6d46e2f62729
Create Date: 2024-08-25 12:34:32.024801

"""
from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e611c6511870'
down_revision: Union[str, None] = '6d46e2f62729'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('group_facebook', 'tags',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('group_facebook', 'tags',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
