
import sqlite3 #this is from the standard libary hence no download needed

DB_FILE = "lost_and_found.db"


def get_connection(): 
    return sqlite3.connect(DB_FILE) #this functionn is needed so every time we want to connect to the database, we can just call this function and it will return a connection object that we can use to interact with the database.


def get_reported_items():
    '''
    Items that have NOT been found yet.
    Rule: ItemStatus is blank/NULL -> still reported/lost.
    '''
    
    conn = get_connection() #to make it easier to connect we call this function conn
    cur = conn.cursor() #this is what actually runs the sql queries and returns the results. The cursor is like a pointer to the database and it is used to execute SQL commands and fetch data from the database.
    #this is like a query it is used to get the data from the database and also the data is sorted in descending order based on the date lost. The query is used to get the data from the database and also the data is sorted in descending order based on the date lost.
    cur.execute(""" 
        SELECT ItemID, ItemName, DateLost, LocationLost, ItemValue
        FROM ItemTable
        WHERE ItemStatus IS NULL OR TRIM(ItemStatus) = ''
        ORDER BY DateLost DESC
    """)
    rows = cur.fetchall() # this ensures that all the data doesnt come back automatically and that when asked for they come back. The fetchall() method is used to fetch all the rows of a query result, returning a list. An empty list is returned when no more rows are available.
    conn.close()
    return rows #sends the lists of tuples back to what ever called this function. The rows variable is a list of tuples, where each tuple represents a row in the result set. Each tuple contains the values for the columns specified in the SELECT statement.


def get_found_items():
    """
    Items that HAVE been found.
    Rule: ItemStatus = 'Found'.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT ItemID, ItemName, DateFound, LocationFound, ItemValue
        FROM ItemTable
        WHERE ItemStatus = 'Found'
        ORDER BY DateFound DESC
    """)
    rows = cur.fetchall()
    conn.close()
    return rows
