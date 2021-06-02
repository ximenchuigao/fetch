import os


def get_db_name():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    dbPath = os.path.join(ROOT_DIR, 'data\\test.db')
    return dbPath


def get_excel_name(name):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    dbPath = os.path.join(ROOT_DIR, 'data\\'+name)
    return dbPath


def get_db_init_fund_details_sql():
    return '''
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
            from_setup  REAL);'''


def get_db_init_funds_industry_sql():
    return '''
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
            industryName, TEXT);'''


def get_db_init_funds_type_sql():
    return '''
        DROP TABLE IF EXISTS Funds;
        CREATE TABLE Funds (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            code  TEXT,
            name TEXT,
            type   TEXT);'''


def get_db_init_funds_manager_sql():
    return '''
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
            all_retribution  REAL);'''
