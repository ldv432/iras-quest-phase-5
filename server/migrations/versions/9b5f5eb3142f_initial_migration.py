"""initial migration

Revision ID: 9b5f5eb3142f
Revises: 
Create Date: 2024-12-11 12:59:24.042867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b5f5eb3142f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('monsters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('health', sa.Integer(), nullable=False),
    sa.Column('power', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('npcs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dialogue', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reaction_type', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('health', sa.Integer(), nullable=False),
    sa.Column('power', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('time', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_players_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('players', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_players_user_id'), ['user_id'], unique=False)

    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=300), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_posts_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_posts_user_id'), ['user_id'], unique=False)

    op.create_table('postreactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('reaction_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name=op.f('fk_postreactions_post_id_posts')),
    sa.ForeignKeyConstraint(['reaction_id'], ['reactions.id'], name=op.f('fk_postreactions_reaction_id_reactions')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_postreactions_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('postreactions', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_postreactions_reaction_id'), ['reaction_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('postreactions', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_postreactions_reaction_id'))

    op.drop_table('postreactions')
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_posts_user_id'))

    op.drop_table('posts')
    with op.batch_alter_table('players', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_players_user_id'))

    op.drop_table('players')
    op.drop_table('users')
    op.drop_table('reactions')
    op.drop_table('npcs')
    op.drop_table('monsters')
    # ### end Alembic commands ###
