"""empty message

Revision ID: 7e5c97b77e33
Revises: 
Create Date: 2020-09-11 11:22:37.921451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e5c97b77e33'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category')
    )
    op.create_table('Questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exam', sa.String(length=1000), nullable=False),
    sa.Column('category', sa.String(length=1000), nullable=False),
    sa.Column('question', sa.String(length=1000), nullable=False),
    sa.Column('question_type', sa.String(length=1000), nullable=False),
    sa.Column('question_image', sa.String(length=1000), nullable=True),
    sa.Column('answer_1', sa.String(length=2000), nullable=False),
    sa.Column('answer_2', sa.String(length=2000), nullable=False),
    sa.Column('answer_3', sa.String(length=2000), nullable=False),
    sa.Column('answer_4', sa.String(length=2000), nullable=False),
    sa.Column('answers', sa.String(length=12000), nullable=False),
    sa.Column('source', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=1000), nullable=False),
    sa.Column('password', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Users')
    op.drop_table('Questions')
    op.drop_table('Categories')
    # ### end Alembic commands ###
