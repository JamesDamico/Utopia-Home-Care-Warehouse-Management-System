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
    return list(c.execute("SELECT * FROM files ORDER BY box_number ASC"))


# Select all data from boxes table
def select_all_from_boxes():
    return list(c.execute("SELECT * FROM boxes ORDER BY box_number ASC"))


# Check if a box number exists 
def box_number_exists(num):
    return list(c.execute(f"SELECT * FROM boxes WHERE box_number IS {num}")) != []


# Return search data
def search_query(table, field, text):
    if field == "box_number":
        return list(c.execute(f"SELECT * FROM {table} WHERE {field} IS {text} ORDER BY box_number ASC"))
    else:
        return list(c.execute(f"SELECT * FROM {table} WHERE UPPER({field}) LIKE('%{text}%') ORDER BY box_number ASC"))


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


##########
# Update #
##########

def update_file(form_data):
    update_query = "UPDATE files SET box_number = ?, type = ?, last_name = ?, first_name = ?, office = ?, year = ? WHERE file_id = ?"
    c.execute(update_query, form_data)
    conn.commit()


def update_box(form_data):
    update_query = "UPDATE boxes SET shelf_number = ? WHERE box_number = ?"
    c.execute(update_query, form_data)
    conn.commit()

    

