from config import db
import sqlite3


class InitDb:
    def __init__(self):
        self.dbname = db.get_db_name()

    def create_funds_table(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.executescript('''
            DROP TABLE IF EXISTS Funds;
            CREATE TABLE Funds (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            code  TEXT,
            name TEXT,
            type   TEXT);''')
        conn.commit()
        cur.close()
        conn.close()
    
    def create_fund_details_table(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.executescript('''
            DROP TABLE IF EXISTS FundDetails;
            CREATE TABLE FundDetails (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            code  TEXT,
            daily_increase   REAL,
            one_week    REAL,
            one_month   REAL,
            three_month REAL,
            six_month   REAL,
            one_year    REAL,
            two_year    REAL,
            three_year  REAL,
            from_thisyear   REAL,
            from_setup  REAL);''')
        conn.commit()
        cur.close()
        conn.close()

    def create_fund_industry_table(self):       
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.executescript('''
            DROP TABLE IF EXISTS FundIndustry;
            CREATE TABLE FundIndustry (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            code  TEXT,
            fun_name  TEXT,
            one_week    REAL,
            one_month   REAL,
            three_month REAL,
            six_month   REAL,
            from_thisyear   REAL,
            one_year    REAL,
            two_year    REAL,
            three_year  REAL,
            industryCode TEXT,
            industryName, TEXT);''')
        conn.commit()
        cur.close()
        conn.close()

    def create_managers_table(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.executescript('''
            DROP TABLE IF EXISTS Managers;
            CREATE TABLE Managers (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            code  TEXT,
            name   TEXT, 
            company_id  TEXT, 
            company_name  TEXT, 
            fun_ids  TEXT, 
            fun_names  TEXT, 
            days  INT, 
            now_best_retribution  REAL, 
            now_best_fun_id  TEXT, 
            now_best_fun_names  TEXT, 
            total_fund  REAL, 
            all_retribution  REAL);''')
        conn.commit()
        cur.close()
        conn.close()

    def create_param_table(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.executescript('''
            DROP TABLE IF EXISTS FundsParams;
            CREATE TABLE FundsParams (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            code  TEXT,
            one_year_bzc  REAL, 
            two_year_bzc  REAL, 
            three_year_bzc  REAL, 
            one_year_xp  REAL, 
            two_year_xp  REAL, 
            three_year_xp  REAL);''')
        conn.commit()
        cur.close()
        conn.close()
    
    def start(self):
        self.create_funds_table();
        self.create_fund_details_table();
        self.create_fund_industry_table();
        self.create_managers_table();
        # self.create_param_table()

