from fund_sync.request_builder.fund_params_builder import FundParamsReq
from fund_sync.response_processor.fund_params_processor import FundParamsProcessor
from common import html_fetch
from config import db
from common.db_query.funds import FundsTable


class FundsParamsTask:
    def do():
        codes = FundsTable().query_all_funds_code()
        for code in codes:
            fund_type_request = FundParamsReq(code)
            content = html_fetch.download(fund_type_request.url)
            processor = FundParamsProcessor([content, code], db.get_db_name())
            processor.process()
