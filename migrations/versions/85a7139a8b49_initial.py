"""Initial

Revision ID: 85a7139a8b49
Revises: 
Create Date: 2022-12-18 23:18:48.572614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85a7139a8b49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
