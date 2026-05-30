from src.features.auth.domaine.user import User as UserEntity, BaseUser
from src.features.auth.repositories.auth_repository import AuthRepository


class AuthService:
    def __init__(self, repo: AuthRepository):
        self.repo: AuthRepository = repo

    async def register_user(self, user: UserEntity):
        """
        DEFINE THE USER CREATION FLOW
        """
        pass
