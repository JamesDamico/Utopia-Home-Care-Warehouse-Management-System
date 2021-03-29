# Import sqlite3
import sqlite3

# Set up the connection 
conn = sqlite3.connect("UHC_Warehouse_db.db")

# Create cursor object
c = conn.cursor()

##########
# SELECT #
##########

# Select all data from files table
def select_all_from_files():
    return list(c.execute("SELECT * FROM files"))


# Select all data from boxes table
def select_all_from_boxes():
    return list(c.execute("SELECT * FROM boxes"))


# Check if a box number exists 
def box_number_exists(num):
    return list(c.execute(f"SELECT * FROM boxes WHERE box_number IS {num}")) != []


# Return search data
def search_query(table, field, text):
    if field == "box_number":
        return list(c.execute(f"SELECT * FROM {table} WHERE {field} IS {text}"))
    else:
        return list(c.execute(f"SELECT * FROM {table} WHERE {field} IS '{text}'"))


##########
# INSERT #
##########

# Add new file
def add_new_file(form_data):
    insert_query = "INSERT INTO files (box_number, type, first_name, last_name, office, year) VALUES (?,?,?,?,?,?)"
    c.execute(insert_query, form_data) 
    conn.commit()


# Add new box
def add_new_box(generate, form_data):
    if generate == "auto":
        print(form_data)
        insert_query = "INSERT INTO boxes (shelf_number) VALUES (?)"
        c.execute(insert_query, form_data)
        conn.commit()
        return c.lastrowid
    elif generate == "manual":
        insert_query = "INSERT INTO boxes (box_number, shelf_number) VALUES (?,?)"    
        c.execute(insert_query, form_data) 
        conn.commit()





    

