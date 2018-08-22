import requestHandler.handler as handler

class DataRequestHandler(handler.RequestHandler):
    id = None

    def __init__(self, id):
        super(DataRequestHandler, self).__init__()
        self.id = id

    def handle(self, request):
        resp = super(DataRequestHandler, self).handle(request)
        try:
            data, perHour = self.db.getDataFromId(self.id)
            self.setContent(self.parser.dataResponse(data, perHour))
            return resp
        except KeyError:
            self.setContent(self.parser.unknownIdError())
            return resp
