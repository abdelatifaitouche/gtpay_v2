from src.features.auth.repositories.auth_repository import AuthRepository
from src.features.auth.services.auth_service import AuthService
from src.infra.db.uow import UnitOfWork


async def get_auth_service():
    uow = UnitOfWork()
    await uow.__aenter__()

    repo = AuthRepository(uow.session)
    service = AuthService(repo)

    try:
        yield service

    except Exception:
        raise
    finally:
        await uow.__aexit__(None, None, None)
    return
