"""Create doctor_application table

Revision ID: 5087c4445c5b
Revises: 7b73d430b14e
Create Date: 2024-10-03 19:55:56.754676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5087c4445c5b'
down_revision = '7b73d430b14e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doctor_application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=100), nullable=False),
    sa.Column('lastname', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phonenumber', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('country', sa.String(length=100), nullable=False),
    sa.Column('cv', sa.String(length=255), nullable=True),
    sa.Column('cover_letter', sa.String(length=255), nullable=True),
    sa.Column('privacy_policy', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('doctor_application')
    # ### end Alembic commands ###
