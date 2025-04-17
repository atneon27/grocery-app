import sqlite3
from models import ProductBody 
from utils.validations import validate_product

# helper functions
# to insert a product
def insert_product(
    db: sqlite3.Connection,
    product: ProductBody 
):
    curr = db.cursor()
    validate_product(curr, product)
    curr.execute(
        "INSERT INTO products (name, price_per_unit, unit) VALUES (?, ?, ?)",
        (product.name, product.price_per_unit, product.unit)
    )
    db.commit()    

# to fetch all existing products
def fetch_products(db: sqlite3.Connection):
    items = []
    curr = db.cursor()
    curr.execute(
        "SELECT * FROM products"
    )
    
    for item in curr.fetchall():
        items.append({
            "product_id": item[0],
            "name": item[1],
            "price_per_unit": item[2],
            "unit": item[3]
        })
    return items

# to fetch a single product
def fetch_product(db: sqlite3.Connection, product_id: str):
    curr = db.cursor()
    curr.execute(
        "SELECT * FROM products WHERE id = ?",
        (product_id,)
    )
    
    item = curr.fetchone()
    return {
        "product_id": item[0],
        "name": item[1],
        "price_per_unit": item[2],
        "unit": item[3]
    }

# to update a product
def find_and_update_product(
    db: sqlite3.Connection,
    product_id: int,
    product: ProductBody
): 
    curr = db.cursor()
    validate_product(curr, product)
    curr.execute(
        "UPDATE products SET name = ?, price_per_unit = ?, unit = ? WHERE id = ?",
        (product.name, product.price_per_unit, product.unit, product_id)
    )
    db.commit()