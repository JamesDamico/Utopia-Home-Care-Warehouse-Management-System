# Import sqlite3
import sqlite3

# Set up the connection 
conn = sqlite3.connect("UHC_Warehouse_db.db")

# Create cursor object
c = conn.cursor()

def select_all_from_files():
    return list(c.execute("SELECT * FROM files"))

def select_all_from_boxes():
    return list(c.execute("SELECT * FROM boxes"))