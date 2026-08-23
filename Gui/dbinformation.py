import sqlite3  # standard library, no install needed
import os

# Build an absolute path to the database, based on where this file
# is located. This way, the database file will always be created next to
DB_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "lost_and_found.db"
)


def get_connection():
    """Opens and returns a connection to the database."""
    return sqlite3.connect(DB_FILE)


def get_reported_items():
    """
    Items that have NOT been found yet.
    Rule: ItemStatus is blank/NULL -> still reported/lost.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT ItemID, ItemName, DateLost, LocationLost, ItemValue
        FROM ItemTable
        WHERE ItemStatus IS NULL OR TRIM(ItemStatus) = ''
        ORDER BY DateLost DESC
    """)
    rows = cur.fetchall()
    conn.close()
    return rows


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


def insert_reported_item(item_name, date_lost, location, item_value):
    """
    Saves a newly reported LOST item to the database.
    Kept separate from the GUI files so Report.py only has to call this
    one function instead of building SQL directly.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO ItemTable
            (ItemName, DateLost, LocationLost, ItemValue, ItemStatus)
        VALUES (?, ?, ?, ?, NULL)
    """, (item_name, date_lost, location, item_value))
    conn.commit()
    conn.close()


def insert_found_item(item_name, date_found, location, item_value):
    """
    Saves a newly reported FOUND item to the database.
    Kept separate from the GUI files so Found.py only has to call this
    one function instead of building SQL directly.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO ItemTable
            (ItemName, DateFound, LocationFound, ItemValue, ItemStatus)
        VALUES (?, ?, ?, ?, 'Found')
    """, (item_name, date_found, location, item_value))
    conn.commit()
    conn.close()
