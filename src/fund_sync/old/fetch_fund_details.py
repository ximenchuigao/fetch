# https://fundapi.eastmoney.com/fundtradenew.aspx?ft=pg&pi=1&pn=100
# response begin with var rankData =

import requests
import demjson
import sqlite3

databaseName = '..\\test.db'


def CreateFundDetailsTable(dbname):
    conn = sqlite3.connect(dbname)
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


def InsertToDb(dbname, data):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('''INSERT OR REPLACE INTO FundDetails
        (code, daily_increase,one_week,one_month,three_month,six_month,one_year,two_year,three_year,from_thisyear,from_setup) 
        VALUES ( ?, ?, ?,?, ?, ?,?, ?, ?,?, ?)''',
                (data[0], data[5], data[6], data[7], data[8],
                 data[9], data[10], data[11], data[12], data[13], data[14]))
    conn.commit()
    cur.close()
    conn.close()


def fetchdata(curpage):

    url = "https://fundapi.eastmoney.com/fundtradenew.aspx?ft=pg&pi={}&pn=100".format(
        curpage)
    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    r = requests.get(url, headers=headers)
    content = r.text
    startIndex = len("var rankData = ")
    search = content[startIndex:]
    search = search[0: len(search)-1]
    dataJson = demjson.decode(search)

    data = dataJson['datas']
    pages = dataJson['allPages']
    curpage = dataJson['pageIndex']
    # data is a list
    for d in data:
        InsertToDb(databaseName, d.split('|'))
    return {"pages": pages, "curpage": curpage}


cur = 1
total = 2
CreateFundDetailsTable(databaseName)
while(cur <= total):
    ret = fetchdata(cur)
    cur = ret["curpage"]+1
    total = ret["pages"]
