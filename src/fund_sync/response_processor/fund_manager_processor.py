import sqlite3
import re
from fund_sync.response_processor.abstract_request_processor import AbstractRequesstProcessor
import demjson


class FundManagerProcessor(AbstractRequesstProcessor):

    def __string_to_int(self, str):
        rest = re.findall("[-+]?[0-9]*\.?[0-9]+", str)
        if len(rest) == 0:
            return 0
        else:
            return rest[0]

    def __insert_to_db(self, data):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute('''INSERT OR REPLACE INTO Managers
            (code, name,company_id,company_name,fun_ids,fun_names,days,now_best_retribution,now_best_fun_id,now_best_fun_names,total_fund,all_retribution) 
            VALUES ( ?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ? )''',
                    (data[0], data[1], data[2], data[3], data[4], data[5], data[6],
                     self.__string_to_int(data[7]), data[8], data[9], self.__string_to_int(data[10]), self.__string_to_int(data[11])))
        conn.commit()
        cur.close()
        conn.close()

    def process(self):
        search = self.content[16:]
        dataJson = demjson.decode(search)
        data = dataJson['data']
        record = dataJson['record']
        pages = dataJson['pages']
        curpage = dataJson['curpage']
        # data is a list
        for d in data:
            self.__insert_to_db(d)
        return {"pages": pages, "curpage": curpage}
