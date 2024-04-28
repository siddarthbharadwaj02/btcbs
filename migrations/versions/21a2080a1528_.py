"""empty message

Revision ID: 21a2080a1528
Revises: 4b28754ef3d0
Create Date: 2024-04-28 11:04:25.391807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21a2080a1528'
down_revision = '4b28754ef3d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attendance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.String(length=100), nullable=False),
    sa.Column('attendance_date', sa.Date(), nullable=False),
    sa.Column('status', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('court',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('cost_per_hour', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('mobile_number', sa.String(length=100), nullable=False),
    sa.Column('totp_secret_key', sa.String(length=36), nullable=False),
    sa.Column('qr_code', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mobile_number')
    )
    op.create_table('booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.String(length=100), nullable=False),
    sa.Column('court_id', sa.Integer(), nullable=False),
    sa.Column('booking_date', sa.Date(), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('end_time', sa.Time(), nullable=False),
    sa.ForeignKeyConstraint(['court_id'], ['court.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booking')
    op.drop_table('user')
    op.drop_table('court')
    op.drop_table('attendance')
    # ### end Alembic commands ###