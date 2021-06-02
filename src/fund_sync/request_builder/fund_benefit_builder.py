from fund_sync.request_builder.abstract_request_builder import AbstractRequestBuilder


class FundBenefitReq(AbstractRequestBuilder):
    def __init__(self, current_page):
        super().__init__();
        self.build_urlparameters(current_page)
        self.url = self.url.format(self.current_page)

    def build_url(self):
        self.url = "https://fundapi.eastmoney.com/fundtradenew.aspx?ft=pg&pi={}&pn=100"

    def build_header(self):
        self.header = {'content-type': 'application/json',
                       'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

    def build_urlparameters(self, current_page):
        self.current_page = current_page