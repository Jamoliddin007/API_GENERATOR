"""commited crud models

Revision ID: ddbd55b41053
Revises: 
Create Date: 2025-04-05 18:00:51.534825

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ddbd55b41053'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('crud_fields')
    op.drop_table('crud_models')
    op.drop_index('ix_projects_id', table_name='projects')
    op.drop_table('projects')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('projects_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('subdomain', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('admin_token', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('client_token', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='projects_pkey'),
    sa.UniqueConstraint('name', name='projects_name_key'),
    sa.UniqueConstraint('subdomain', name='projects_subdomain_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_projects_id', 'projects', ['id'], unique=False)
    op.create_table('crud_models',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('crud_models_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], name='crud_models_project_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='crud_models_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('crud_fields',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('nullable', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('format', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('crud_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['crud_id'], ['crud_models.id'], name='crud_fields_crud_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='crud_fields_pkey')
    )
    # ### end Alembic commands ###
