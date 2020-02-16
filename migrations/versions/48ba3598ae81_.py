"""empty message

Revision ID: 48ba3598ae81
Revises: 
Create Date: 2020-02-16 18:42:30.050792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48ba3598ae81'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('resellers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('cpf', sa.String(length=11), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('resellers')
    # ### end Alembic commands ###
