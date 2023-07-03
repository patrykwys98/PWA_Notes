"""adding tag to note

Revision ID: 1727084f57a3
Revises: a253019e2ae4
Create Date: 2023-03-20 15:12:23.934578

"""
import sqlalchemy as sa
import sqlalchemy_utils

from alembic import op

# revision identifiers, used by Alembic.
revision = '1727084f57a3'
down_revision = 'a253019e2ae4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note', sa.Column('tag', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('note', 'tag')
    # ### end Alembic commands ###