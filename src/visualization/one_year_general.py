from common.db_query.fund_industry import FundIndustry
from common.excel_generator.one_year_general_generator import OneYearGeneralGenerator
from common.excel_factory import ExcelFactory

class OneYearGeneral:
    def do(self):
        data = FundIndustry().query_one_year_industry_general()
        tableGenerator = OneYearGeneralGenerator(data)
        ExcelFactory.CreatExcel(
            "fun_detais_one_year.xlsx", "one_year", tableGenerator)
