# ------------------------------------------------------------------------ #
# Title: Query GageInsight Database
# Description: sqlite query returning (gage_id, desc, company, serial_num, manufacturer, model_num, cert_template)

# ------------------------------------------------------------------------ #
import sqlite3
from sqlite3 import Error


class QueryGage:

    @staticmethod
    def create_connection():
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(r"C:\Users\alcom\Documents\otv_v2\GageInsight.db")
        except Error as e:
            print(e)

        return conn

    # TODO: what if there are more than one item per gage_ID?
    @staticmethod
    def select_item(conn, gid):
        """
        Select item from gage
        :param conn: the Connection object
        :param gid: string for gage id
        :return: rows
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM GAGE WHERE gage_id = " + "'" + gid + "'")

        rows = cur.fetchall()
        row = rows[0]

        return row

    # unpack a tuple with all item information into assigned variables.
    @staticmethod
    def get_gage_id():
        gid = input("Gage ID: ").strip().upper()
        return gid

    @staticmethod
    def fetch(gid):
        # # connect to DB
        conn = QueryGage.create_connection()

        # create item
        item = QueryGage.select_item(conn, gid)
    #
        return item
    # # # unpack item
    # # (gage_id, desc, company, serial_num, manufacturer, model_num, cert_template) = item
    #
    # (Item.gage_id, Item.desc, Item.company, Item.serial_num, Item.mfg, Item.model_num, Item.cert_template) = item
