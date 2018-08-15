
class DummyRequest:
    headers = {}
    data = ''

    def __init__(self):
        self.headers['User-Agent'] = "esp-idf/1.0 esp32"
