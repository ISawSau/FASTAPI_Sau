from sqlmodel import SQLModel, Field

class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class ProductRequest(SQLModel):
    id: int
    name: str
    category: str
    price: int
    company: str # sensible
    pattern: int # sensible

class ProductResponse(SQLModel):
    id: int
    name: str

class ProductPartialResponse(SQLModel):
    id: int
    name: str

class ProductUpdateName(SQLModel):
    name: str

class ProductUpdateTwoFields(SQLModel):
    name: str
    description: str