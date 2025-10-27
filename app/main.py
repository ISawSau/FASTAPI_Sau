from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

#a
load_dotenv()
#b
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
#c
SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/user", response_model=dict, tags=["CREATE"])
def addUser(user: UserRequest,db:Session = Depebds(get_db)):
    insert_user = User.model_validate(user)
    db.add(insert_user)
    db.commit()
    return {"msg":"Afegit usuari correctament"}

@app.get("user/{id}", response_model=UserResponse, tags=["READ by ID"])
def getUser(id: int, db:Session = Depends(get_db)):
    stmt = select(User).where(User.id == id)
    result = db.exec(stmt.first())
    return UserResponse.model_validate(result)

"""@app.post("/api/users", response_model = dict)
async def createUser():
    newUser = {"id": len(users) + 1, "name": "nomUsuari", "email": "email@iticbcn.cat"}
    users.append(newUser)
    return{"users": users}

@app.get("/api/users/{id}", response_model = dict)
async def readUserById(id: int):
    for user in users:  
        if user["id"] == id:
            return{"user": user}
    return{"user": None}

@app.get("/api/users", response_model = dict)
async def readAllUsers():
    return{"users": users}

@app.put("/api/users/{id}", response_model = dict)
async def updateUser(id: int):
    for user in users:
        if user["id"] == id:
            user["name"] = "nomActualitzat"
            user["email"] = "emailNou@iticbcn.cat"
    return{"users": users}


@app.patch("api/users/{id}", response_model = dict)
async def partialUserUpdate(id : int):
    #
    return{"users": "usuari parcialment actualitzat"}


@app.delete("/api/users/{id}", response_model = dict)
async def deleteUser(id: int):
    userFound = None
    for user in users:
        if user["id"] == id:
            userFound = user
    if userFound:
        users.remove(userFound)
    return{"users": users}"""