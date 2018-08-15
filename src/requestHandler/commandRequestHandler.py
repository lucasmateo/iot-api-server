import requestHandler.handler as handler
from flask import request
from constant import COMMANDS
from json import dumps

class CommandRequestHandler(handler.RequestHandler):
    command = None
    form_label_id = "id"
    commandLabel = "command"

    def __init__(self, command):
        super(CommandRequestHandler, self).__init__()
        self.command = command

    def handle(self, request):
        resp = super(CommandRequestHandler, self).handle(request)
        print("Command=" + self.command)
        print("ID=" + request.form[self.form_label_id])
        device_id = request.form[self.form_label_id]
        self.db.addCommand(device_id, self.command)
        return resp