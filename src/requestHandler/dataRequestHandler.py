import requestHandler.handler as handler

class DataRequestHandler(handler.RequestHandler):
    id = None

    def __init__(self, id):
        super(DataRequestHandler, self).__init__()
        self.id = id

    def handle(self, request):
        resp = super(DataRequestHandler, self).handle(request)
        try:
            data = self.db.getDataFromId(self.id)
            resp.data = self.parser.dataResponse(data)
            return resp
        except KeyError:
            resp.data = self.parser.unknownIdError()
            return resp