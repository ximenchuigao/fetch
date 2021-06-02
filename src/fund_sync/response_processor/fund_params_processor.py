import sqlite3
import re
from fund_sync.response_processor.abstract_request_processor import AbstractRequesstProcessor
from bs4 import BeautifulSoup


class FundParamsProcessor(AbstractRequesstProcessor):
    def __string_to_int(self, str):
        rest = re.findall("[-+]?[0-9]*\.?[0-9]+", str)
        if len(rest) == 0:
            return 0
        else:
            return rest[0]

    def __insert_to_db(self, code, bzc, xp):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute('''INSERT OR REPLACE INTO FundsParams
            (code, one_year_bzc,two_year_bzc,three_year_bzc,one_year_xp,two_year_xp,three_year_xp) 
            VALUES ( ?, ?, ?, ?, ?, ?, ?)''',
                    (code, self.__string_to_int(bzc[0]),
                     self.__string_to_int(bzc[1]),
                     self.__string_to_int(bzc[2]),
                     self.__string_to_int(xp[0]),
                     self.__string_to_int(xp[1]),
                     self.__string_to_int(xp[2])))
        conn.commit()
        cur.close()
        conn.close()

    def process(self):
        try:
            soup = BeautifulSoup(self.content[0])
            table = soup.find(attrs={'class': 'fxtb'})
            for row in table.findAll("tr"):
                cells = row.findAll("td")
                print(len(cells))
                if len(cells) != 4:
                    continue
                if cells[0].text == "标准差":
                    bzc = [cells[1].text, cells[2].text, cells[3].text]
                if cells[0].text == "夏普比率":
                    xp = [cells[1].text, cells[2].text, cells[3].text]
            print(bzc)
            print(xp)
            self.__insert_to_db(self.content[1], bzc, xp)
        except:
            return
