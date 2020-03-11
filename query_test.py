import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


# TODO: how to assign each column in the query return to a variable.
def select_item(conn, gage_id):
    """
    Select item from gage
    :param conn: the Connection object
    :param gage_id: string for gage id
    :return: rows
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM GAGE WHERE gage_id = " + "'" + gage_id + "'")

    rows = cur.fetchall()
    asset = rows[0]

    return asset

# unpack a tuple with all item information into assigned variables.


def main():
    database = r"C:\Users\alcom\Documents\otv_v2\GageInsight.db"

    # create a database connection
    conn = create_connection(database)
    g_id = str(input("GAGE ID: ").upper())
    with conn:
        item = select_item(conn, g_id)
        (gage_id, desc, company, serial_num, manufacturer, model_num, cert_template) = item
        print("Item: ")
        print(gage_id)
        print()


if __name__ == '__main__':
    main()
