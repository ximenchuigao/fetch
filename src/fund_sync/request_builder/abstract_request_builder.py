# Abstract class
class AbstractRequestBuilder:
    def __init__(self):
        self.build_url()
        self.build_header()

    def build_url(self):
        return

    def build_urlparameters(self, parameters=None):
        return

    def build_header(self):
        return

    def __repr__(self):
        return 'fetch data: {0.url} , {0.header}'.format(self)
