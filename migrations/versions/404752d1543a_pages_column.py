"""pages_column

Revision ID: 404752d1543a
Revises: 85a7139a8b49
Create Date: 2022-12-18 23:26:24.137394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '404752d1543a'
down_revision = '85a7139a8b49'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('pages', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'pages')
    # ### end Alembic commands ###