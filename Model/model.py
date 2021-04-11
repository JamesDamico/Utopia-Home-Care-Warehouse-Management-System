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
    """
    Returns all files in the database in ascending order.
    """
    return list(c.execute("SELECT * FROM files ORDER BY box_number ASC"))


# Select all data from boxes table
def select_all_from_boxes():
    """
    Returns all boxes in the database in ascending order.
    """
    return list(c.execute("SELECT * FROM boxes ORDER BY box_number ASC"))


# Check if a box number exists 
def box_number_exists(num):
    """
    Returns True or False based on whether a box exists or not.
    """
    return list(c.execute(f"SELECT * FROM boxes WHERE box_number IS {num}")) != []


# Return search data
def search_query(table, field, text):
    """
    Returns data the user searched for.

    Takes in table (boxes/files), a field, and the specific text.
    """
    if field == "box_number":
        return list(c.execute(f"SELECT * FROM {table} WHERE {field} IS {text} ORDER BY box_number ASC"))
    else:
        return list(c.execute(f"SELECT * FROM {table} WHERE UPPER({field}) LIKE('%{text}%') ORDER BY box_number ASC"))


##########
# INSERT #
##########

# Add new file
def add_new_file(form_data):
    """
    Inserts a file into the database.

    Takes in form_data as the data being entered.
    """
    insert_query = "INSERT INTO files (box_number, type, first_name, last_name, office, year) VALUES (?,?,?,?,?,?)"
    c.execute(insert_query, form_data) 
    conn.commit()


# Add new box
def add_new_box(generate, form_data):
    """
    Inserts a box into the database.

    Takes in form_data as the data being entered.
    """
    if generate == "auto":
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
    """
    Updates a file in the database.

    Takes in form_data as the data being updated.
    """
    update_query = "UPDATE files SET box_number = ?, type = ?, last_name = ?, first_name = ?, office = ?, year = ? WHERE file_id = ?"
    c.execute(update_query, form_data)
    conn.commit()


def update_box(form_data):
    """
    Updates a box in the database.

    Takes in form_data as the data being updated.
    """
    update_query = "UPDATE boxes SET shelf_number = ? WHERE box_number = ?"
    c.execute(update_query, form_data)
    conn.commit()

def set_box_number_null(box_num):
    """
    Sets box_number to null where box_number is box_num.
    """
    update_query = f"UPDATE files SET box_number = 'NULL' WHERE box_number = {box_num}"
    c.execute(update_query)
    conn.commit()

##########
# Delete #
##########

def delete_file(file_id):
    """
    Delete file where file_id matches parameter.
    """
    delete_query = f"DELETE FROM files WHERE file_id = {file_id}"
    c.execute(delete_query)
    conn.commit()


def delete_box(box_num):
    """
    Delete box where box_num matches parameter.
    """
    delete_query = f"DELETE FROM boxes WHERE box_number = {box_num}"
    c.execute(delete_query)
    conn.commit()


def delete_all_files(box_num):
    """
    Delete all files where box_num matches parameters.
    """
    delete_query = f"DELETE FROM files WHERE box_number = {box_num}"
    c.execute(delete_query)
    conn.commit()
