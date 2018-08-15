import requestHandler.idRequestHandler as idHandler
import requestHandler.measureRequestHandler as measureHandler
from flask import request, Blueprint

deviceBp = Blueprint('deviceGateways', __name__)

@deviceBp.route('/device/id', methods = ['GET'])
def getNewId():
    return idHandler.IdRequestHandler().handle(request)


@deviceBp.route('/device/measure', methods = ['POST'])
def giveReadings():
    return measureHandler.MeasureRequestHandler().handle(request)
