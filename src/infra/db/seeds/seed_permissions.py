from sqlalchemy.ext.asyncio import AsyncSession
from .permissions import get_all_permissions
from src.features.auth.models.permissions import Permission
from sqlalchemy.dialects.postgresql import insert as pg_insert

"""
    RUN THIS SCRIPT IN AN ASYNCIO EVENT LOOP
    
    Idomptement Script using pg insert.value.on_conflict_do_nothing()

    Input : 
        - an open Session/connection 
        - rollback/commit/close from where you called this script

    Script : 
        - using the get_all_permission() method at src.infra.db.seeds.permissions
            - catches all new permissions defined at each feature 
            - packed inside the The class Permission in src.core.permissions
                - each Feature Permissions should be added in its own class class ResourcePermission and imported in 
                    src.core.permissions

        - builds the format sqlalchemy/ permission table format : (resource , action , scope)


"""


async def seed_permissions(session: AsyncSession):

    all_perms = get_all_permissions()

    data_to_insert = [
        {"resource": r, "action": a, "scope": s.value} for r, a, s in all_perms
    ]

    result = await session.execute(
        pg_insert(Permission).values(data_to_insert).on_conflict_do_nothing()
    )

    return result
