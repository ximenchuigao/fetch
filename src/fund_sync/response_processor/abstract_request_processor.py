class AbstractRequesstProcessor:
    def __init__(self, content, db_name):
        self.build_db(db_name)
        self.build_content(content)
        return

    def build_db(self, db_name):
        self.db_name = db_name
    
    def build_content(self, content):
        self.content = content

    def process():
        return
