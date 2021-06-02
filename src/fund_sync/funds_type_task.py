from fund_sync.request_builder.fund_type_req_builder import FundTypeReq
from fund_sync.response_processor.fund_type_processor import FundTypeProcessor
import requests
from config import db


class FundsTypeTask:
    def do():
        fund_type_request = FundTypeReq()
        r = requests.get(fund_type_request.url,
                         headers=fund_type_request.header)
        content = r.text
        processor = FundTypeProcessor(content, db.get_db_name())
        processor.process()
