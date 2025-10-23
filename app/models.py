from typing import Optional
from sqlmodel import SQLModel, Field

# taula BD
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str

# crear un nou usuari
class UserCreate(SQLModel):
    name: str
    email: str

# retornar dades usuari
class UserResponse(SQLModel):
    id: int
    name: str
    email: str