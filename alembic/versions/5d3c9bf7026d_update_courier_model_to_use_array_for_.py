"""Update Courier model to use ARRAY for districts

Revision ID: 5d3c9bf7026d
Revises: 
Create Date: 2024-05-28 21:00:55.320299

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d3c9bf7026d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_orders_id', table_name='orders')
    op.drop_index('ix_orders_name', table_name='orders')
    op.drop_table('orders')
    op.drop_index('ix_couriers_id', table_name='couriers')
    op.drop_index('ix_couriers_name', table_name='couriers')
    op.drop_table('couriers')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('couriers',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('districts', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='couriers_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_couriers_name', 'couriers', ['name'], unique=False)
    op.create_index('ix_couriers_id', 'couriers', ['id'], unique=False)
    op.create_table('orders',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('district', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('courier_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('status', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['courier_id'], ['couriers.id'], name='orders_courier_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='orders_pkey')
    )
    op.create_index('ix_orders_name', 'orders', ['name'], unique=False)
    op.create_index('ix_orders_id', 'orders', ['id'], unique=False)
    # ### end Alembic commands ###