"""initial commit

Revision ID: a1795679c1d3
Revises: 
Create Date: 2023-11-28 21:36:54.223410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1795679c1d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=70), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('architect',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('image', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=40), nullable=False),
    sa.Column('biography', sa.Text(), nullable=True),
    sa.Column('architect_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['architect_id'], ['architect.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.Column('city', sa.String(length=20), nullable=True),
    sa.Column('country', sa.String(length=30), nullable=False),
    sa.Column('architect_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['architect_id'], ['architect.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    op.drop_table('bio')
    op.drop_table('architect')
    op.drop_table('admin')
    # ### end Alembic commands ###
