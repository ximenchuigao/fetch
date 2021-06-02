import requests
import demjson
import sqlite3
import re

# This script is used to fetch data from tiantian fund to get all managers information
databaseName = '..\\test.db'


def fetchdata(curpage):
    url = "http://fund.eastmoney.com/Data/FundDataPortfolio_Interface.aspx?dt=14&mc=returnjson&ft=all&pi={}".format(
        curpage)
    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    r = requests.get(url, headers=headers)
    content = r.text
    search = content[16:]

    dataJson = demjson.decode(search)

    data = dataJson['data']
    record = dataJson['record']
    pages = dataJson['pages']
    curpage = dataJson['curpage']
    # data is a list
    for d in data:
        InsertToDb(databaseName, d)
    return {"pages": pages, "curpage": curpage}


def InsertToDb(dbname, data):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('''INSERT OR REPLACE INTO Managers
        (code, name,company_id,company_name,fun_ids,fun_names,days,now_best_retribution,now_best_fun_id,now_best_fun_names,total_fund,all_retribution) 
        VALUES ( ?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ? )''',
                (data[0], data[1], data[2], data[3], data[4], data[5], data[6], StringToInt(data[7]), data[8], data[9], StringToInt(data[10]), StringToInt(data[11])))
    conn.commit()
    cur.close()
    conn.close()


def StringToInt(str):
    rest = re.findall("[-+]?[0-9]*\.?[0-9]+", str)
    if len(rest) == 0:
        return 0
    else:
        return rest[0]


def CreateManagersTable(dbname):
    print(111)
    conn = sqlite3.connect(dbname)
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


cur = 0
total = 1
CreateManagersTable(databaseName)
while(cur <= total):
    ret = fetchdata(cur)
    cur = ret["curpage"]+1
    total = ret["pages"]


# print(data)
