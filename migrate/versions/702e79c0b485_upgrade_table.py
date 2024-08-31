"""upgrade table

Revision ID: 702e79c0b485
Revises: 2781d51b5781
Create Date: 2024-08-31 13:30:48.246194

"""
from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '702e79c0b485'
down_revision: Union[str, None] = '2781d51b5781'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment_facebook', sa.Column('owner_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('comment_facebook', sa.Column('owner_link', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.drop_column('comment_facebook', 'onwer_link')
    op.drop_column('comment_facebook', 'onwer_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment_facebook', sa.Column('onwer_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('comment_facebook', sa.Column('onwer_link', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('comment_facebook', 'owner_link')
    op.drop_column('comment_facebook', 'owner_name')
    # ### end Alembic commands ###
