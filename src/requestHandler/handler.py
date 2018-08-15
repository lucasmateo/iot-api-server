import abc
import flask
import parser.jsonParser
import database.database as database

"""
super class of all request handler
"""
class RequestHandler(abc.ABC):
    parser = None
    db = None

    def __init__(self):
        self.db = database.Database.getDatabase()
        self.parser = parser.jsonParser.JsonParser()

    """
    format the response with the right headers common to all response
    """
    @abc.abstractmethod
    def handle(self,request):
        response = flask.Response()
        response.mimetype = 'application/json'
        del response.headers['Server']
        return response

    def setParser(self,parser):
        self.parser = parser
