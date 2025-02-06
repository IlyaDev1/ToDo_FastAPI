"""add primary key to table

Revision ID: f4e11d8180e3
Revises: 43bde5b1adc4
Create Date: 2025-02-06 07:51:44.552102

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4e11d8180e3'
down_revision: Union[str, None] = '43bde5b1adc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'id', existing_type=sa.Integer(), primary_key=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'id', existing_type=sa.Integer(), primary_key=False)
    # ### end Alembic commands ###
