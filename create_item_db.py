# ------------------------------------------------------------------------ #
# Title: Create Item DB
# Description: Creates DB from exported excel file from Indysoft

# ------------------------------------------------------------------------ #
import sqlite3
from sqlite3 import Error
import pandas as pd


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


# creates a table in the database
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


# create item to place in db
def create_item(conn, xlpath, tablename):
    df = pd.read_excel(xlpath, index_col=0, usecols="A,D,G:J,L")     # usecols="A:C, E" to take only the columns I want
    """
    Create a new item into the items table
    :param conn:
    :param xlpath: input path to the excel file with all the data
    :param: tablename: name of the table with all of the excel data
    :return: (gage_id, desc, company, serial_num, manufacturer, model_num, cert_template)db
    """
    df.to_sql(name=tablename, con=conn, if_exists="append")


def main():
    database = r"C:\Users\alcom\Documents\otv_v2\GageInsight.db"
    excel = r"C:\Users\alcom\Documents\otv_v2\Inventory_all_031020.xlsx"

    # sql_create_items = """ CREATE TABLE IF NOT EXISTS items (
    #                                     gage_id text PRIMARY KEY,
    #                                     model_num NOT NULL,
    #                                     serial_num text NOT NULL,
    #                                     mfg text NOT NULL,
    #                                     Desc text NOT NULL
    #                                 ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        # create_table(conn, sql_create_items)
        create_item(conn, excel, "GAGE")

        # # create tasks table
        # create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()



