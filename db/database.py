import sqlite3

create_product_table = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price_per_unit REAL,
        unit TEXT
    );
'''

create_order_table = '''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        customer_name TEXT,
        product_id INTEGER,
        quantity INTEGER,
        FOREIGN KEY (product_id) REFERENCES products(id)
    );
'''

# to provider a connection to the database to every route
def get_db():
    conn = sqlite3.connect('db/grocery.db')
    try:
        yield conn
    finally:
        conn.close()

# to setup the database on startup
def setup_db(db: sqlite3.Connection):
    curr = db.cursor()
    curr.execute(create_product_table)
    curr.execute(create_order_table)
    db.commit()


    