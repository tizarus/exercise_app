"""Added Exercise Model

Revision ID: 89288b6d1695
Revises: 
Create Date: 2024-09-17 15:00:42.923337

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '89288b6d1695'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercise', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.alter_column('primary',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('secondary',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('function',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('mechanics',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('equipment',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('directions',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=3000),
               existing_nullable=True)
        batch_op.drop_index('ix_exercise_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercise', schema=None) as batch_op:
        batch_op.create_index('ix_exercise_id', ['id'], unique=False)
        batch_op.alter_column('directions',
               existing_type=sa.String(length=3000),
               type_=mysql.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('equipment',
               existing_type=sa.String(length=50),
               type_=mysql.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('mechanics',
               existing_type=sa.String(length=50),
               type_=mysql.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('function',
               existing_type=sa.String(length=50),
               type_=mysql.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('secondary',
               existing_type=sa.String(length=50),
               type_=mysql.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('primary',
               existing_type=sa.String(length=50),
               type_=mysql.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.String(length=100),
               type_=mysql.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###