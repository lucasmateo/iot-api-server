import requestHandler.handler as handler

from constant import COMMANDS
from json import dumps

class CommandListRequestHandler(handler.RequestHandler):

    def handle(self, request):
        resp = super(CommandListRequestHandler, self).handle(request)
        resp.data = dumps(COMMANDS)
        return resp