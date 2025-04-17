import sqlite3
from models import ProductBody, OrderBody

def validate_product(curr: sqlite3.Cursor, product: ProductBody):
    count = curr.execute(
        "SELECT COUNT(*) FROM products WHERE name = ?",
        (product.name,)
    )

    prod_cnt = count.fetchone()[0]

    if prod_cnt > 0:
        raise ValueError("Product name is not unique")
    if product.price_per_unit < 0:
        raise ValueError("Price per unit is negetive")
    
def validate_order(curr: sqlite3.Cursor, product_id: int, quatnity: int):
    count = curr.execute(
        "SELECT COUNT(*) FROM products WHERE id = ?",
        (product_id, )
    )

    order_cnt = count.fetchone()[0]
    
    if order_cnt == 0:    
        raise ValueError("Product dose not exist")
    if quatnity < 0:    
        raise ValueError("Quantity is negative")