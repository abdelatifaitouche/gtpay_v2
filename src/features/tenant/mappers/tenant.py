from src.features.tenant.schemas.tenant import CreateTenant
from src.features.tenant.domaine.tenant import CreateTenant as CreateTenantEntity


class TenantMapper:
    @staticmethod
    def from_create_schema(data: CreateTenant) -> CreateTenantEntity:
        return CreateTenantEntity(
            name=data.name,
            type=data.type,
        )
