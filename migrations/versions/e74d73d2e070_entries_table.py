"""entries table

Revision ID: e74d73d2e070
Revises: f70ce2a6bb66
Create Date: 2021-05-20 13:37:19.157712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e74d73d2e070'
down_revision = 'f70ce2a6bb66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_handover_owner', table_name='handover')
    op.drop_index('ix_handover_platform', table_name='handover')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_handover_platform', 'handover', ['platform'], unique=False)
    op.create_index('ix_handover_owner', 'handover', ['owner'], unique=False)
    # ### end Alembic commands ###
