from fund_sync.request_builder.fund_manager_builder import FundManagerReq
from fund_sync.response_processor.fund_manager_processor import FundManagerProcessor
import requests
from config import db


class FundsManagerTask:
    def do():
        current_page = 1
        fund_type_request = FundManagerReq(current_page)
        r = requests.get(fund_type_request.url,
                         headers=fund_type_request.header)
        content = r.text
        processor = FundManagerProcessor(content, db.get_db_name())
        result = processor.process()
        total = result["pages"]
        while(current_page <= total):
            current_page = current_page+1
            fund_type_request = FundManagerReq(current_page)
            r = requests.get(fund_type_request.url,
                         headers=fund_type_request.header)
            content = r.text
            processor = FundManagerProcessor(content, db.get_db_name())
            result = processor.process()
            total = result["pages"]
