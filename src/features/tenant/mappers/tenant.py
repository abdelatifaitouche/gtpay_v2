from src.features.tenant.schemas.tenant import CreateTenant, UpdateTenant

from src.features.tenant.domaine.tenant import (
    CreateTenant as CreateTenantEntity,
    TenantUpdate as TenantUpdateDTO,
)


class TenantMapper:
    @staticmethod
    def from_create_schema(data: CreateTenant) -> CreateTenantEntity:
        return CreateTenantEntity(
            name=data.name,
            type=data.type,
        )

    @staticmethod
    def to_update_dto(schema: UpdateTenant) -> TenantUpdateDTO:
        data = schema.model_dump(exclude_unset=True)
        print(data)
        return TenantUpdateDTO(**data)
