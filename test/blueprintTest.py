import context
import unittest
import blueprints.deviceBlueprint as deviceBp
import blueprints.webBlueprint as webBp
import requestHandler.measureRequestHandler as measureHandler
import dummy.dummyRequest
import database.database as db
import constant
import parser.jsonParser as parser
import json

from requestHandler.commandRequestHandler import CommandRequestHandler

class BlueprintTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        db.Database.getDatabase().connect(constant.testDb)


    @classmethod
    def tearDown(self):
        database = db.Database.getDatabase()
        database.clearDatabase()

    @classmethod
    def tearDownClass(self):
        db.Database.getDatabase().disconnect()

    def test_list(self):
        deviceBp.getNewId()
        deviceBp.getNewId()
        deviceBp.getNewId()

        resp = webBp.getDeviceList()

        data = parser.JsonParser().getData(resp.data)

        self.assertEqual(3,len(data))

    def test_data(self):
        id = deviceBp.getNewId().get_json()['id']

        request =dummy.dummyRequest.DummyRequest()
        request.data = json.dumps({"id":id,"val":True})
        measureHandler.MeasureRequestHandler().handle(request)

        data = parser.JsonParser().getData(webBp.getDeviceData(id).data)

        print(data)
        self.assertEqual(1,len(data))
        self.assertEqual(True,data[0]['state'])

    def test_data_array(self):
        id = deviceBp.getNewId().get_json()['id']

        request =dummy.dummyRequest.DummyRequest()
        request.data = json.dumps({"id":id,"val":[0,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]})
        measureHandler.MeasureRequestHandler().handle(request)

        data = parser.JsonParser().getData(webBp.getDeviceData(id).data)

        print(data)
        self.assertEqual(26,len(data))
        self.assertEqual(False,data[0]['state'])
        self.assertEqual(False,data[1]['state'])
        self.assertEqual(False,data[2]['state'])
        self.assertEqual(True,data[3]['state'])
        self.assertEqual(True,data[4]['state'])
        self.assertEqual(True,data[5]['state'])
        self.assertEqual(False,data[6]['state'])
        self.assertEqual(True,data[7]['state'])
        self.assertEqual(False,data[8]['state'])

    @unittest.skip("parsing error")
    def test_AddCommand(self):
        command = "testing_command"
        req = dummy.dummyRequest.DummyRequest()
        id = deviceBp.getNewId().get_json()['id']

        req.data = "id=" + id
        CommandRequestHandler(command).handle(req)
        dab = db.Database.getDatabase()
        self.assertEqual(dab.getCommandList()[0], command)

    def test_noSuchId(self):
        data = webBp.getDeviceData('fffff').get_json()
        self.assertEqual(constant.statusKO,data[constant.statusLabel])

if __name__ == '__main__':
    unittest.main()
