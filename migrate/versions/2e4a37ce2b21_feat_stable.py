"""feat(stable)

Revision ID: 2e4a37ce2b21
Revises: fe7b188233b9
Create Date: 2024-09-10 22:00:29.245451

"""
from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e4a37ce2b21'
down_revision: Union[str, None] = 'fe7b188233b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('group_facebook', 'link')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('group_facebook', sa.Column('link', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
