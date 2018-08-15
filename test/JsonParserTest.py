import unittest
import context
import json

import parser.jsonParser

class JsonParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.parser = parser.jsonParser.JsonParser()

    def test_idResponse(self):
        result = self.parser.idResponse(True,'hello')
        self.assertEqual(json.loads(result),json.loads(json.dumps({"status" : "OK", "id" : "hello"})))

    def test_getMeasureInfo(self):
        result = self.parser.getMeasureInfo(json.dumps({"id" : "hello", "val" : True}))

        self.assertEqual("hello",result[0])
        self.assertEqual([True],result[1])

if __name__ == '__main__':
    unittest.main()
