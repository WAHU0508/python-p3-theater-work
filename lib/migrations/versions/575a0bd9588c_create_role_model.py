"""Create Role Model

Revision ID: 575a0bd9588c
Revises: ae35a08be390
Create Date: 2024-09-13 00:22:18.612675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '575a0bd9588c'
down_revision = 'ae35a08be390'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    # ### end Alembic commands ###
