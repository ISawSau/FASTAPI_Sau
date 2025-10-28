from sqlmodel import SQLModel, Field

class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    id: int
    name: str

class ProductRequest(SQLModel):
    name: str

class ProductResponse(SQLModel):
    id: int
    name: str