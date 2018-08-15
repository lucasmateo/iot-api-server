import context
import unittest
import requestHandler.idRequestHandler as handler
import dummy.dummyDb as db
import dummy.dummyRequest as request

import json

class IdRequestHandlerTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.handler = handler.IdRequestHandler()
        self.handler.db = db.DummyDB()

    @classmethod
    def setUpClass(self):
        self.handler = handler.IdRequestHandler()
        self.handler.db = db.DummyDB()

    def test_getID(self):
        req = request.DummyRequest()
        response = self.handler.handle(req)
        js = json.loads(response.data)
        self.assertEqual("OK",js['status'])
        self.assertEqual(db.dummyId,js['id'])

if __name__ == '__main__':
    unittest.main()
