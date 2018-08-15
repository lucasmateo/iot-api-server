import requestHandler.handler as handler

class IdRequestHandler(handler.RequestHandler):

    def handle(self, request):
        resp = super(IdRequestHandler, self).handle(request)
        id = self.db.createNewDevice()
        resp.data = self.parser.idResponse(True,id)
        return resp
