"""update table

Revision ID: 049905d67c83
Revises: 4a218069e0a3
Create Date: 2024-12-07 13:02:49.122497

"""
from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '049905d67c83'
down_revision: Union[str, None] = '4a218069e0a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('user_id', sa.Uuid(), nullable=False))
    op.drop_column('comment', 'userId')
    op.add_column('group', sa.Column('user_id', sa.Uuid(), nullable=False))
    op.drop_column('group', 'userId')
    op.add_column('history_scrape', sa.Column('user_id', sa.Uuid(), nullable=False))
    op.drop_column('history_scrape', 'userId')
    op.add_column('post', sa.Column('user_id', sa.Uuid(), nullable=False))
    op.drop_column('post', 'userId')
    op.add_column('template_message', sa.Column('user_id', sa.Uuid(), nullable=False))
    op.drop_column('template_message', 'userId')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('template_message', sa.Column('userId', sa.UUID(), autoincrement=False, nullable=False))
    op.drop_column('template_message', 'user_id')
    op.add_column('post', sa.Column('userId', sa.UUID(), autoincrement=False, nullable=False))
    op.drop_column('post', 'user_id')
    op.add_column('history_scrape', sa.Column('userId', sa.UUID(), autoincrement=False, nullable=False))
    op.drop_column('history_scrape', 'user_id')
    op.add_column('group', sa.Column('userId', sa.UUID(), autoincrement=False, nullable=False))
    op.drop_column('group', 'user_id')
    op.add_column('comment', sa.Column('userId', sa.UUID(), autoincrement=False, nullable=False))
    op.drop_column('comment', 'user_id')
    # ### end Alembic commands ###