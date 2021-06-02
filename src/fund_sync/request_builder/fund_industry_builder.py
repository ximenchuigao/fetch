from fund_sync.request_builder.abstract_request_builder import AbstractRequestBuilder


class FundIndustryReq(AbstractRequestBuilder):
    def __init__(self, current_page, item_code):
        super().__init__()
        self.build_urlparameters(current_page, item_code)
        self.url = self.url.format(self.item_code, self.current_page)

    def build_url(self):
        self.url = "http://fund.eastmoney.com/data/FundGuideapi.aspx?dt=4&sd=&ed=&tp={}&sc=3y&st=desc&pi={}&pn=100&zf=diy&sh=list"

    def build_header(self):
        self.header = {'content-type': 'application/json',
                       'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

    def build_urlparameters(self, current_page, item_code):
        self.current_page = current_page
        self.item_code = item_code
