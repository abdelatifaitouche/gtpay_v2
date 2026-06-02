from src.core.role_permissions import ROLE_PERMISSIONS
from sqlalchemy.ext.asyncio import AsyncSession
from src.features.auth.models.roles import Role
from src.features.auth.models.permissions import Permission
from sqlalchemy import select, insert
from src.features.auth.models.role_permission import RolePermission
from sqlalchemy.dialects.postgresql import insert as pg_insert


async def fetch_data(session: AsyncSession, model):
    """
    Helper function to fetch data from the db :
        input :
            - an open session/connection
            - model name

        output :
            - list of tuples from the db
    """

    stmt = select(model)

    result = await session.execute(stmt)

    data = result.scalars().all()
    return data


async def seed_role_permissions(session: AsyncSession):
    """
    Role_permissions Seeding
    it does a lot of work am lazy just read it its simple
    """
    roles_data = await fetch_data(session, Role)

    if not roles_data:
        raise Exception(
            "No Roles Found, run seed roles first at src.infra.db.seed.seed_role"
        )

    roles_map = {r.name: r.id for r in roles_data}

    permissions_data = await fetch_data(session, Permission)

    if not permissions_data:
        raise Exception(
            "No Permissions Found, run seed permissions at src.infra.db.seed.seed_permissions"
        )

    permissions_map = {
        (
            p.resource,
            p.action,
            p.scope,
        ): p.id
        for p in permissions_data
    }

    data_insert = []
    for role, permissions in ROLE_PERMISSIONS.items():
        if len(permissions) == 0:
            continue
        r_id = roles_map[role.value]
        for p in permissions:
            r, a, s = p
            p_id = permissions_map[
                (
                    r,
                    a,
                    s.value,
                )
            ]
            data_insert.append({"role_id": r_id, "permission_id": p_id})

    await session.execute(
        pg_insert(RolePermission).values(data_insert).on_conflict_do_nothing()
    )
