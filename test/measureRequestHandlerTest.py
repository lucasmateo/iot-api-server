import context
import unittest
import requestHandler.measureRequestHandler as handler
import dummy.dummyDb as db
import dummy.dummyRequest as request
import constant
import json

class MeasureRequestHandlerTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.handler = handler.MeasureRequestHandler()
        self.handler.db = db.DummyDB()

    def test_measureHandle(self):
        req = request.DummyRequest()
        req.data = json.dumps({"id":"hello","val":True})
        response = self.handler.handle(req)
        self.assertEqual(json.loads('{"status" : "OK","command":[]}'),json.loads(response.data))



if __name__ == '__main__':
    unittest.main()
