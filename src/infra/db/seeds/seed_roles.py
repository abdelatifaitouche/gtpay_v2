from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.features.auth.models.roles import Role
from src.core.roles import ROLES

"""
    RUN THIS IN AN ASYNCIO EVENT LOOP
    
    Idompotent : using the pg insert.values.on_conflict_do_nothing()

    Input : 
        - an open connection/session to database
        - commit/rollback/close from where you call this script

    Script description : 
        Gets the List of tuple (ROLE,SCOPE) from src.core.roles 

        builds the sqlalchemy insert format depending on the Role Table (name , scope , is_system)

        Run this script only at init of the deployment to populate the Role Table

        to setup for the SUPERADMIN Creation

"""


async def seed_roles(session: AsyncSession):
    all_roles = [
        {"name": n.value, "scope": s.value, "is_system": True} for n, s in ROLES
    ]
    result = await session.execute(
        pg_insert(Role).values(all_roles).on_conflict_do_nothing()
    )

    return result
