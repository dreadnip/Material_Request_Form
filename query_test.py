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


def select_item(conn, gage_id):
    """
    Select item from gage
    :param conn: the Connection object
    :param gage_id: string for gage id
    :return: rows
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM GAGE WHERE gage_id = " + gage_id + ';')

    rows = cur.fetchall()

    return rows


def main():
    database = r"C:\Users\alcom\Documents\otv_v2\GageInsight.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("item: ")
        select_item(conn, 'A4455')


if __name__ == '__main__':
    main()
