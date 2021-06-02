from fund_sync.request_builder.abstract_request_builder import AbstractRequestBuilder

class FundTypeReq(AbstractRequestBuilder):
    def build_url(self):
        self.url = "http://fund.eastmoney.com/js/fundcode_search.js"

    def build_header(self):
        self.header = {'content-type': 'application/json',
                       'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

    def build_urlparameters(self):
        return
