import sqlite3
from models import OrderBody
from utils.validations import validate_order

#helper fucntions
# to insert an order
def insertOrder(
    db: sqlite3.Connection,
    order: OrderBody
):
    curr = db.cursor()

    for item in order.items: 
        validate_order(curr, item.product_id, item.quantity)  
        curr.execute(
            "INSERT INTO orders (customer_name, product_id, quantity) VALUES (?, ?, ?)",
            (order.customer_name, item.product_id, item.quantity)
        )
        
    db.commit()

# to fetch all existing orders
def fetch_orders(db: sqlite3.Connection):
    orders_dict = {}
    curr = db.cursor()

    curr.execute("""
        SELECT 
            orders.id AS order_id,
            orders.customer_name,
            orders.product_id,
            products.name AS product_name,
            orders.quantity,
            products.price_per_unit
        FROM orders
        INNER JOIN products ON orders.product_id = products.id
    """)

    rows = curr.fetchall()

    for row in rows:
        order_id, customer_name, product_id, product_name, quantity, price_per_unit = row
        item_price = quantity * price_per_unit

        if order_id not in orders_dict:
            orders_dict[order_id] = {
                "order_id": order_id,
                "customer_name": customer_name,
                "items": [],
                "total_price": 0
            }

        orders_dict[order_id]["items"].append({
            "product_id": product_id,
            "product_name": product_name,
            "quantity": quantity,
            "price": item_price
        })

        orders_dict[order_id]["total_price"] += item_price

    return list(orders_dict.values())

# to fetch a single order
def fetch_order(db: sqlite3.Connection, order_id: str):
    curr = db.cursor()
    curr.execute("""
        SELECT 
            orders.id AS order_id,
            orders.customer_name,
            orders.product_id,
            products.name AS product_name,
            orders.quantity,
            products.price_per_unit
        FROM orders
        INNER JOIN products ON orders.product_id = products.id WHERE orders.id = ?      
    """, (order_id,))
    
    row = curr.fetchone()
    order_id, customer_name, product_id, product_name, quantity, price_per_unit = row
    item_price = quantity * price_per_unit
    return {
        "order_id": order_id,
        "customer_name": customer_name,
        "items": [{
            "product_id": product_id,
            "product_name": product_name,
            "quantity": quantity,
            "price": item_price
        }],
        "total_price": item_price
    }