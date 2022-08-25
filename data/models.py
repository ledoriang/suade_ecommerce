from importlib.resources import path
import sqlite3
import os

PATH = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(PATH, "csv")


class DBManager:
    
    def read_data(self, filename, table):
        with sqlite3.connect("ecommerce.db") as connection:
            c = connection.cursor()
            file = open(filename, "r", encoding="utf-8-sig")
            file.readline()
            for line in file:
                line = line.split(",")
                if isinstance(line[-1], str):
                    line[-1] = line[-1].rstrip()
                valuePattern = "(" + ",".join(["?"] * len(line)) + ")"
                c.execute("INSERT INTO "+table+" VALUES "+valuePattern, line)
            file.close()


    def db_create(self):
    # Create a new database if the database doesn't already exist
        with sqlite3.connect("ecommerce.db") as connection:
            c = connection.cursor()
            # Create the promotions table 
            c.execute("""CREATE TABLE IF NOT EXISTS promotions(
                ID INTEGER PRIMARY KEY,
                Description TEXT
                )""")
            # Create the products table 
            c.execute("""CREATE TABLE IF NOT EXISTS products(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Description TEXT
                )""")
            # Create the product_promotions table 
            c.execute("""CREATE TABLE IF NOT EXISTS product_promotions(
                date DATE,
                product_id INTEGER,
                promotion_id INTEGER,
                FOREIGN KEY (product_id) REFERENCES products(ID),
                FOREIGN KEY (promotion_id) REFERENCES promotions(ID)
                )""")
            # Create the commisions table 
            c.execute("""CREATE TABLE IF NOT EXISTS commissions(
                date DATE,
                vendor_id INTEGER,
                rate FLOAT
                )""")
            # Create the orders table 
            c.execute("""CREATE TABLE IF NOT EXISTS orders(
                ID INTEGER PRIMARY KEY,
                created_at DATETIME,
                vendor_id INTEGER,
                customer_id INTEGER
                )""")
            # Create the order_lines table
            c.execute("""CREATE TABLE IF NOT EXISTS order_lines(
                order_id INTEGER,
                product_id INTEGER,
                product_description TEXT,
                product_price FLOAT,
                product_vat_rate FLOAT,
                discount_rate FLOAT,
                quantity INTEGER,
                full_price_amount FLOAT,
                discounted_amount FLOAT,
                vat_amount FLOAT,
                total_amount FLOAT,
                FOREIGN KEY (order_id) REFERENCES orders(ID),
                FOREIGN KEY (product_id) REFERENCES products(ID)
                )""")

if __name__ == "__main__":
    # Setup initial db
    db = DBManager()
    db.db_create()
    db.read_data(os.path.join(CSV_PATH, "promotions.csv"), "promotions")
    db.read_data(os.path.join(CSV_PATH, "products.csv"), "products")
    db.read_data(os.path.join(CSV_PATH, "product_promotions.csv"), "product_promotions")
    db.read_data(os.path.join(CSV_PATH, "commissions.csv"), "commissions")
    db.read_data(os.path.join(CSV_PATH, "orders.csv"), "orders")
    db.read_data(os.path.join(CSV_PATH, "order_lines.csv"), "order_lines")


