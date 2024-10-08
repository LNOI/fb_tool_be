"""update code

Revision ID: d7a7f16df402
Revises: 283ead9a1de1
Create Date: 2024-08-27 22:18:41.203376

"""
from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd7a7f16df402'
down_revision: Union[str, None] = '283ead9a1de1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post_facebook', sa.Column('video', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.add_column('post_facebook', sa.Column('reaction', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.alter_column('post_facebook', 'post_date',
               existing_type=postgresql.TIMESTAMP(),
               type_=sqlmodel.sql.sqltypes.AutoString(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post_facebook', 'post_date',
               existing_type=sqlmodel.sql.sqltypes.AutoString(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    op.drop_column('post_facebook', 'reaction')
    op.drop_column('post_facebook', 'video')
    # ### end Alembic commands ###
