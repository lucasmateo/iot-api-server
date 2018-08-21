import requestHandler.handler as handler

class ListRequestHandler(handler.RequestHandler):

    def handle(self, request):
        data = self.db.getDeviceList()
        resp = super(ListRequestHandler, self).handle(request)
        self.setContent(self.parser.listResponse(data))
        return resp
