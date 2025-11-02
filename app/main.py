from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session, select
from dotenv import load_dotenv
import os

from app.models.Product import Product, ProductRequest, ProductResponse, ProductPartialResponse, ProductUpdateName, ProductUpdateTwoFields

# carregar variables d'entorn
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)  # crear taules

# connexió a la BD
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/product", response_model=dict, tags=["CREATE"])
def addProduct(product: ProductRequest, db: Session = Depends(get_db)):
    insert_product = Product.model_validate(product)
    db.add(insert_product)
    db.commit()
    db.refresh(insert_product)
    return {"msg": "Afegit producte correctament"}

@app.get("/product/{id}", response_model=ProductResponse, tags=["READ by ID"])
def getProduct(id: int, db: Session = Depends(get_db)):
    stmt = select(Product).where(Product.id == id)
    result = db.exec(stmt).first()
    return ProductResponse.model_validate(result)

@app.get("/products", response_model=list[ProductResponse], tags=["READ ALL"])
def getAllProducts(db: Session = Depends(get_db)):
    stmt = select(Product)
    results = db.exec(stmt).all()
    return [ProductResponse(id=product.id, name=product.name) for product in results]

@app.get("/products/name/{name}", response_model=list[ProductResponse], tags=["READ FILTERED"])
def getProductsByName(name: str, db: Session = Depends(get_db)):
    stmt = select(Product).where(Product.name == name)
    results = db.exec(stmt).all()
    return [ProductResponse(id=product.id, name=product.name) for product in results]

@app.delete("/product/delete/{id}", response_model=dict, tags=["DELETE"])
def deleteProduct(id: int, db: Session = Depends(get_db)):
    stmt = select(Product).where(Product.id == id)
    product = db.exec(stmt).first()
    db.delete(product)
    db.commit()
    return {"msg": f"Producte amb ID {id} eliminat correctament"}

@app.get("/product/partial/{id}", response_model=ProductPartialResponse, tags=["READ PARCIAL"])
def getProductPartial(id: int, db: Session = Depends(get_db)):
    stmt = select(Product).where(Product.id == id)
    result = db.exec(stmt).first()
    return ProductPartialResponse(id=result.id, name=result.name)

@app.put("/product/{id}", response_model=dict, tags=["UPDATE TOTAL"])
def updateProductTotal(id: int, product: ProductRequest, db: Session = Depends(get_db)):
    stmt = select(Product).where(Product.id == id)
    db_product = db.exec(stmt).first()
    db_product.name = product.name
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return {"msg": f"Producte amb ID {id} actualitzat completament"}

@app.patch("/product/{id}/name", response_model=dict, tags=["UPDATE PARCIAL 1 CAMP"])
def updateProductName(id: int, product_update: ProductUpdateName, db: Session = Depends(get_db)):
    stmt = select(Product).where(Product.id == id)
    db_product = db.exec(stmt).first()
    db_product.name = product_update.name
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return {"msg": f"Nom del producte amb ID {id} actualitzat"}

@app.patch("/product/{id}/two-fields", response_model=dict, tags=["UPDATE PARCIAL 2 CAMPS"])
def updateProductTwoFields(id: int, product_update: ProductUpdateTwoFields, db: Session = Depends(get_db)):
    stmt = select(Product).where(Product.id == id)
    db_product = db.exec(stmt).first()
    db_product.name = product_update.name
    db_product.description = product_update.description
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return {"msg": f"Producte amb ID {id} actualitzat amb dos camps"}