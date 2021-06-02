import builtins
from fund_sync.request_builder.abstract_request_builder import AbstractRequestBuilder


class FundParamsReq(AbstractRequestBuilder):

    def __init__(self, code):
        self.build_urlparameters(code)
        super().__init__()

    def build_url(self):
        self.url = 'http://fundf10.eastmoney.com/tsdata_{}.html'
        self.url = self.url.format(self.code)

    def build_header(self):
        return

    def build_urlparameters(self, code):
        self.code = code
