from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session, select
from dotenv import load_dotenv
import os

from app.models.Product import Product,ProductRequest,ProductResponse

#a
load_dotenv()
#b
DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)
engine = create_engine(DATABASE_URL)
# #c
SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/product", response_model=dict, tags=["CREATE"])
def addProduct(product: ProductRequest,db:Session = Depends(get_db)):
    insert_product = Product.model_validate(product)
    db.add(insert_product)
    db.commit()
    return {"msg":"Afegit usuari correctament"}

@app.get("/product/{id}", response_model=ProductResponse, tags=["READ by ID"])
def getProduct(id: int, db:Session = Depends(get_db)):
    stmt = select(Product).where(Product.id == id)
    result = db.exec(stmt).first()
    return ProductResponse.model_validate(result)

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