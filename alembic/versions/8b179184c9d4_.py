"""empty message

Revision ID: 8b179184c9d4
Revises: 
Create Date: 2024-08-01 16:06:10.055703

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '8b179184c9d4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient_table',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('lotus_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('fio', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('is_man', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('lotus_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patient_table')
    # ### end Alembic commands ###