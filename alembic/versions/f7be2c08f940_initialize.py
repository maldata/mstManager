"""initialize

Revision ID: f7be2c08f940
Revises: 
Create Date: 2017-02-08 22:12:58.603209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7be2c08f940'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('media_sets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('seasons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seasonNumber', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('episodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('season_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['season_id'], ['seasons.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('number')
    )
    op.create_table('media_collection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('episode_id', sa.Integer(), nullable=False),
    sa.Column('media_set_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['episode_id'], ['episodes.id'], ),
    sa.ForeignKeyConstraint(['media_set_id'], ['media_sets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('media_collection')
    op.drop_table('episodes')
    op.drop_table('seasons')
    op.drop_table('media_sets')
    # ### end Alembic commands ###