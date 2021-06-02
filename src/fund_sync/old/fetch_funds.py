# http://fund.eastmoney.com/js/fundcode_search.js

import requests
import demjson
import sqlite3
import re

databaseName = '..\\test.db'
def CreateFundsTable(dbname):
    conn = sqlite3.connect(dbname)
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


def InsertToDb(dbname, data):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('''INSERT OR REPLACE INTO Funds
        (code, name,type) 
        VALUES ( ?, ?, ?)''',
                (CleanUp(data[0]), CleanUp(data[2]), CleanUp(data[3])))
    conn.commit()
    cur.close()
    conn.close()
def fetchdata():
    url = "http://fund.eastmoney.com/js/fundcode_search.js"
    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    r = requests.get(url, headers=headers)
    content = r.text
    startIndex = len("var r = ")
    search = content[startIndex:] 

    search = search[1: len(search)-2]
    dataJson = re.findall(r"\[(.*?)\]", search)
    #data is a list
    for d in dataJson:
        InsertToDb(databaseName, d.split(','))


def CleanUp(data):
    rest = re.findall("\"(.*?)\"", data)
    return rest[0]

CreateFundsTable(databaseName)
fetchdata()
