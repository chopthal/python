"""empty message

Revision ID: 1d4702ef70e0
Revises: 731f40264252
Create Date: 2021-04-23 14:31:02.575823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d4702ef70e0'
down_revision = '731f40264252'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_question_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_question_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
