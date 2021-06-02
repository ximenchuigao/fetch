import sqlite3
import re
from fund_sync.response_processor.abstract_request_processor import AbstractRequesstProcessor


class FundTypeProcessor(AbstractRequesstProcessor):
    def __clean_up(self, data):
        rest = re.findall("\"(.*?)\"", data)
        return rest[0]

    def __insert_to_db(self, data):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute('''INSERT OR REPLACE INTO Funds
            (code, name,type) 
            VALUES ( ?, ?, ?)''',
                    (self.__clean_up(data[0]), self.__clean_up(data[2]), self.__clean_up(data[3])))
        conn.commit()
        cur.close()
        conn.close()

    def process(self):
        startIndex = len("var r = ")
        search = self.content[startIndex:]

        search = search[1: len(search)-2]
        dataJson = re.findall(r"\[(.*?)\]", search)
        # data is a list
        for d in dataJson:
            self.__insert_to_db(d.split(','))
