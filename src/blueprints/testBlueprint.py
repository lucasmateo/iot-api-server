from flask import Blueprint
import json


testBp = Blueprint('test',__name__)

@testBp.route('/device/id/test', methods = ['GET'])
def getNewIdTest():
    return json.dumps({'status':'OK','id':'hello'})


@testBp.route('/device/measure/test', methods = ['POST'])
def giveReadingsTest():
    return '{}'
