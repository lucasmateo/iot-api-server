import context
import unittest
import database.CloudantDb as database
import json
import constant
import datetime

class cloudantDbTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.db = database.db()
        self.db.connect(constant.testDb)

    @classmethod
    def tearDown(self):
        self.db.clearDatabase()
        self.db.disconnect()

    def test_createDevice(self):
        id = self.db.createNewDevice()
        self.assertIsInstance(id,str)

        data = self.db.getDataFromId(id)

        jData = json.loads(json.dumps(data))
        self.assertEqual(json.loads("[]"),jData)

    def test_addData(self):
        id = self.db.createNewDevice()
        self.db.addData(id,True)
        self.db.addData(id,True)

        data = self.db.getDataFromId(id)
        self.assertEqual(2,len(data))

        self.assertEqual(True, data[0]['state'])
        self.assertEqual(True, data[1]['state'])

    def test_addDataArray(self):
        id = self.db.createNewDevice()
        time = datetime.datetime.now()
        self.db.addDataArray(id,[(True,time),(False,time)])

        data = self.db.getDataFromId(id)
        self.assertEqual(2,len(data))

        self.assertEqual(True, data[0]['state'])
        self.assertEqual(False, data[1]['state'])

    def test_getDeviceList(self):
        id = self.db.createNewDevice()
        id2 = self.db.createNewDevice()

        deviceList = self.db.getDeviceList()

        self.assertEqual(2,len(deviceList))

    def test_getDataFromId(self):
        id = self.db.createNewDevice()
        for i in range(5):
            self.db.addData(id,True)

        data = self.db.getDataFromId(id)

        for i in range(5):
            self.assertEqual(True,data[i]['state'])

    def test_AddCommand(self):
        id = self.db.createNewDevice()
        self.db.addCommand(id,"test")

        commlist = self.db.getCommandList(id);
        self.assertEqual("test",commlist[0])

        self.db.deleteCommands(id)
        commlist =self.db.getCommandList(id);
        self.assertEqual(0,len(commlist))





if __name__ == '__main__':
    unittest.main()
