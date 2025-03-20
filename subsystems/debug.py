class Debug:
    def __init__(self):
        self.log = []
    def post(self, data):
        self.log.append(data)
    def detail(self):
        print(self.log)
        self.log.clear()