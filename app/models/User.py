from sqlmodel import, Field

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str

class UserRequest(SQLModel):
    name: str
    lastname: str
    age: int
    passwd: str

class UserResponse(SQLModel):
    id: int
    name: str
    lastname: str
    age: int