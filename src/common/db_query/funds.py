from config import db
import sqlite3


class FundsTable:
    def __init__(self):
        self.dbname = db.get_db_name()

    def query_all_funds_code(self):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        print("Opened database successfully")
        # headings = []
        cursor = c.execute("select code from Funds")
        data = []
        for row in cursor:
            data.append(row[0])
        return data
