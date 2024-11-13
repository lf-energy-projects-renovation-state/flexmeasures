"""create_data_sources_table

Revision ID: 5d39829d91af
Revises: b087ce8b529f
Create Date: 2018-07-09 17:17:36.276000

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5d39829d91af"
down_revision = "b087ce8b529f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "data_sources",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("label", sa.String(length=80), nullable=True),
        sa.Column("type", sa.String(length=80), nullable=True),
        sa.Column("source_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["source_id"], ["bvp_users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column("power", sa.Column("data_source", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "power", "data_sources", ["data_source"], ["id"])
    op.add_column("price", sa.Column("data_source", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "price", "data_sources", ["data_source"], ["id"])
    op.add_column("weather", sa.Column("data_source", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "weather", "data_sources", ["data_source"], ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "weather", type_="foreignkey")
    op.drop_column("weather", "data_source")
    op.drop_constraint(None, "price", type_="foreignkey")
    op.drop_column("price", "data_source")
    op.drop_constraint(None, "power", type_="foreignkey")
    op.drop_column("power", "data_source")
    op.drop_table("data_sources")
    # ### end Alembic commands ###