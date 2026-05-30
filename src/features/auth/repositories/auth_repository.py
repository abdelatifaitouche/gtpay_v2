from sqlalchemy.ext.asyncio import AsyncSession
from src.features.auth.domaine.user import User as UserEntity, BaseUser
from src.features.auth.models.user import User as UserDB


class AuthRepository:
    def __init__(self, db: AsyncSession):
        self.db: AsyncSession = db

    def to_orm(self, user: UserEntity) -> UserDB:
        return UserDB(id=user.id, email=user.email, password_hash=user.password_hash)

    def to_domain(self, orm: UserDB) -> BaseUser:
        return BaseUser(
            id=orm.id,
            email=orm.email,
        )

    async def create_user(self, user: UserEntity) -> BaseUser:
        orm = self.to_orm(user)
        self.db.add(orm)
        await self.db.flush()
        return self.to_domain(orm)
