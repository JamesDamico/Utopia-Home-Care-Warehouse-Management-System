# Import sqlite3
import sqlite3

# Set up the connection 
conn = sqlite3.connect("UHC_Warehouse_db.db")

# Create cursor object
c = conn.cursor()

# Select all data from files table
def select_all_from_files():
    return list(c.execute("SELECT * FROM files"))

# Select all data from boxes table
def select_all_from_boxes():
    return list(c.execute("SELECT * FROM boxes"))

# Add new file
def add_new_file(form_data):
    insert_query = "INSERT INTO files (box_number, type, last_name, first_name, office, year) VALUES (?,?,?,?,?,?)"
    #insert_query = "INSERT INTO files (box_number, type, last_name, first_name, office, year) VALUES (5, 'test', 'test', 'test', 'test', 'test')"
    c.execute(insert_query, form_data) 
    conn.commit()

# Check if a box number exists 
def box_number_exists(num):
    return list(c.execute(f"SELECT * FROM boxes WHERE box_number IS {num}")) != []

    

