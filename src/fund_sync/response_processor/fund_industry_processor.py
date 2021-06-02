import sqlite3
import re
from fund_sync.response_processor.abstract_request_processor import AbstractRequesstProcessor
import demjson


class FundIndustryProcessor(AbstractRequesstProcessor):

    def __insert_to_db(self, data, code, name):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute('''INSERT OR REPLACE INTO FundIndustry
            (code, fun_name, from_thisyear, one_week,one_month,three_month,six_month, one_year,two_year,three_year, industryCode, industryName) 
            VALUES ( ?, ?, ?,?, ?, ?,?, ?, ?,? , ?,? )''',
                    (data[0], data[1], data[4], data[5], data[6], data[7],
                     data[8], data[9], data[10], data[11], code, name))
        conn.commit()
        cur.close()
        conn.close()

    def process(self, code, name):
        startIndex = len("var rankData =")
        search = self.content[startIndex:]
        search = search[0: len(search)]
        dataJson = demjson.decode(search)

        data = dataJson['datas']
        pages = dataJson['allPages']
        curpage = dataJson['pageIndex']
        # data is a list
        for d in data:
            self.__insert_to_db(d.split(','), code, name)
        return {"pages": pages, "curpage": curpage}
