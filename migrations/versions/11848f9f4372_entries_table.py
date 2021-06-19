"""entries table

Revision ID: 11848f9f4372
Revises: eb701d363477
Create Date: 2021-05-20 13:39:16.441005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11848f9f4372'
down_revision = 'eb701d363477'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('handover',
    sa.Column('ho_id', sa.Integer(), nullable=False),
    sa.Column('ticket', sa.String(length=64), nullable=False),
    sa.Column('ticket_type', sa.String(length=64), nullable=False),
    sa.Column('servers', sa.String(length=300), nullable=False),
    sa.Column('platform', sa.Integer(), nullable=True),
    sa.Column('steps', sa.String(length=300), nullable=False),
    sa.Column('next_steps', sa.String(length=300), nullable=False),
    sa.Column('chat_url', sa.String(length=300), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.Column('old_owners', sa.String(length=300), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('ho_id')
    )
    op.create_index(op.f('ix_handover_chat_url'), 'handover', ['chat_url'], unique=False)
    op.create_index(op.f('ix_handover_next_steps'), 'handover', ['next_steps'], unique=False)
    op.create_index(op.f('ix_handover_old_owners'), 'handover', ['old_owners'], unique=False)
    op.create_index(op.f('ix_handover_servers'), 'handover', ['servers'], unique=False)
    op.create_index(op.f('ix_handover_steps'), 'handover', ['steps'], unique=False)
    op.create_index(op.f('ix_handover_ticket'), 'handover', ['ticket'], unique=False)
    op.create_index(op.f('ix_handover_ticket_type'), 'handover', ['ticket_type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_handover_ticket_type'), table_name='handover')
    op.drop_index(op.f('ix_handover_ticket'), table_name='handover')
    op.drop_index(op.f('ix_handover_steps'), table_name='handover')
    op.drop_index(op.f('ix_handover_servers'), table_name='handover')
    op.drop_index(op.f('ix_handover_old_owners'), table_name='handover')
    op.drop_index(op.f('ix_handover_next_steps'), table_name='handover')
    op.drop_index(op.f('ix_handover_chat_url'), table_name='handover')
    op.drop_table('handover')
    # ### end Alembic commands ###
