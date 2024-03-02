from pydantic import BaseModel, Field


class BaseTypeProductSchemas(BaseModel):
    name: str
    description: str


class ReadTypeProductSchemas(BaseTypeProductSchemas):
    id: int


class BaseProductSchemas(BaseModel):
    name: str
    description: str
    price: str
    equipment: str
    count: int
    status: bool
    photo: str
    type_products_id: int

    

class ReadProductSchemas(BaseProductSchemas):
    id: int


class BaseCartSchemas(BaseModel):
    user_id: str
    product_id: int
    
    

class ReadCartSchemas(BaseCartSchemas):
    id: int


# class BaseApplicationsServicesSchemas(BaseModel):
#     short_name: str = Field(min_length=4, max_length=100)
#     full_name: str = Field(min_length=4, max_length=300)
#     technological_process: str
#     code: str
#     mnemonics: str
#     priority: int
#     activity: bool
#     master_id: int
#     active_worker_id: int
