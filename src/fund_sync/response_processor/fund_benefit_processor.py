import sqlite3
import re
from fund_sync.response_processor.abstract_request_processor import AbstractRequesstProcessor
import demjson


class FundBenefitProcessor(AbstractRequesstProcessor):

    def __insert_to_db(self, data):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute('''INSERT OR REPLACE INTO FundDetails
            (code, daily_increase,one_week,one_month,three_month,six_month,one_year,two_year,three_year,from_thisyear,from_setup) 
            VALUES ( ?, ?, ?,?, ?, ?,?, ?, ?,?, ?)''',
                    (data[0], data[5], data[6], data[7], data[8],
                     data[9], data[10], data[11], data[12], data[13], data[14]))
        conn.commit()
        cur.close()
        conn.close()

    def process(self):
        startIndex = len("var rankData = ")
        search = self.content[startIndex:]
        search = search[0: len(search)-1]
        dataJson = demjson.decode(search)

        data = dataJson['datas']
        pages = dataJson['allPages']
        curpage = dataJson['pageIndex']
        # data is a list
        for d in data:
            self.__insert_to_db(d.split('|'))
        return {"pages": pages, "curpage": curpage}
