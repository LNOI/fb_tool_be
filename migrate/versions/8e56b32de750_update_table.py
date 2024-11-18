"""update table

Revision ID: 8e56b32de750
Revises: 62648b005839
Create Date: 2024-11-17 17:11:26.455582

"""
from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e56b32de750'
down_revision: Union[str, None] = '62648b005839'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history_scrape', sa.Column('num_groups', sa.Integer(), nullable=True))
    op.add_column('history_scrape', sa.Column('num_posts', sa.Integer(), nullable=True))
    op.add_column('history_scrape', sa.Column('num_comments', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('history_scrape', 'num_comments')
    op.drop_column('history_scrape', 'num_posts')
    op.drop_column('history_scrape', 'num_groups')
    # ### end Alembic commands ###
