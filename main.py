from fastapi import FastAPI

app = FastAPI()

users = []

@app.post("/api/users", response_model = dict)
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

"""
@app.patch("api/users/{id}", response_model = dict)
async def partialUserUpdate(id : int):
    #
    return{"users": "usuari parcialment actualitzat"}
"""

@app.delete("/api/users/{id}", response_model = dict)
async def deleteUser(id: int):
    userFound = None
    for user in users:
        if user["id"] == id:
            userFound = user
    if userFound:
        users.remove(userFound)
    return{"users": users}