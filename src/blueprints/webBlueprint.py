from flask import request, Blueprint

from requestHandler.commandRequestHandler import CommandRequestHandler
from requestHandler.commandlistRequestHandler import CommandListRequestHandler

import requestHandler.dataRequestHandler as dataHandler
import requestHandler.listRequestHandler as listHandler

webBp = Blueprint('webGateway', __name__)

@webBp.route('/api/device_list', methods = ['GET'])
def getDeviceList():
    return listHandler.ListRequestHandler().handle(request)


@webBp.route('/api/device_data/<id>', methods = ['GET'])
def getDeviceData(id):
    return dataHandler.DataRequestHandler(id).handle(request)

@webBp.route('/api/command/<command>', methods = ['POST'])
def getCommand(command):
    return CommandRequestHandler(command).handle(request)

@webBp.route('/api/command_list', methods = ['GET'])
def getCommandList():
    return CommandListRequestHandler().handle(request)
    