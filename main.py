import sqlite3
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routes.orders import router as order_router    
from routes.products import router as product_router
from db import setup_db

app = FastAPI(
    title="Grocery App",
    description="A simple grocery app", 
)

# to setup the database on startup
@app.on_event("startup")
def startup_event():
    db = sqlite3.connect("db/grocery.db")
    setup_db(db)

app.add_middleware(
    CORSMiddleware
)

app.include_router(order_router)
app.include_router(product_router)