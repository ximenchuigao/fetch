from fund_sync.request_builder.fund_benefit_builder import FundBenefitReq
from fund_sync.response_processor.fund_benefit_processor import FundBenefitProcessor
import requests
from config import db


class FundsBenefitTask:
    def do():
        current_page = 1
        fund_type_request = FundBenefitReq(current_page)
        r = requests.get(fund_type_request.url,
                         headers=fund_type_request.header)
        content = r.text
        processor = FundBenefitProcessor(content, db.get_db_name())
        result = processor.process()
        total = result["pages"]
        while(current_page <= total):
            current_page = current_page+1
            fund_type_request = FundBenefitReq(current_page)
            content = r.text
            processor = FundBenefitProcessor(content, db.get_db_name())
            result = processor.process()
            total = result["pages"]