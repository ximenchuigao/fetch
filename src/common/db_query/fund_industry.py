from config import db
import sqlite3


class FundIndustry:
    def __init__(self):
        self.dbname = db.get_db_name()

    def query_one_year_industry_general(self):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        print("Opened database successfully")
        cursor = c.execute(
            "select code ,industryName, fun_name,  max(one_year) as maxval from FundIndustry WHERE one_year is not null and one_year != '' group by FundIndustry.industryCode")
        data = []
        val = []
        industry = []
        for row in cursor:
            val.append(row[3])
            industry.append(row[2]+'-'+row[1]+'('+row[0]+')')
        data.append(val)
        data.append(industry)
        return data
    

    def query_two_year_industry_general(self):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        print("Opened database successfully")
        cursor = c.execute(
            "select code ,industryName, fun_name,  max(one_year) as maxval from FundIndustry WHERE one_year is not null and one_year != '' group by FundIndustry.industryCode")
        data = []
        val = []
        industry = []
        for row in cursor:
            val.append(row[3])
            industry.append(row[2]+'-'+row[1]+'('+row[0]+')')
        data.append(val)
        data.append(industry)
        return data
