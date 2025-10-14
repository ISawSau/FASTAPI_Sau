from fastapi import FastAPI

app = FastAPI()

users = []

@app.post("/api/users", response_model = dict)
async def createUser():
    #
    return{"users": users}

@app.get("/api/users/{id}", response_model = dict)
async def readUserById(id: int):
    #
    return{"userData": "dades de l'usuari"}

@app.get("/api/users", response_model = dict)
async def readAllUsers():
    #
    return{"users": users}

@app.put("api/users/{id}", response_model = dict)
async def updateUser(id: int):
    #
    return{"users": "usuari actualizat"}

@app.patch("api/users/{id}", response_model = dict)
async def partialUserUpdate(id : int):
    #
    return{"users": "usuari parcialment actualitzat"}

@app.delete("api/users/{id}", response_model = dict)
async def deleteUser(id: int):
    #
    return{"users": users}