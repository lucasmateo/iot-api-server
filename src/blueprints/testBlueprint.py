from flask import Blueprint
import json
import flask

testBp = Blueprint('test',__name__)

@testBp.route('/device/id/test', methods = ['GET'])
def getNewIdTest():
    response = flask.Response()
    response.mimetype = 'application/json'
    response.set_data(json.dumps({'status':'OK','id':'hello'}))
    response.headers.add('Length',len(json.dumps({'status':'OK','id':'hello'})))
    print(response)
    return response


@testBp.route('/device/measure/test', methods = ['POST'])
def giveReadingsTest():
    return '{}'
