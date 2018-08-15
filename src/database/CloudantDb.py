import os
from cloudant import Cloudant
import sched
from cloudant.document import Document
import json
import datetime
import constant
"""
Cloudant database implementation
"""
class db:
    dataLabel = "data"
    timeLabel = "stamp"
    statusLabel = "state"
    lastUpdateLabel = 'lastUpdate'
    commandLabel = "command"



    def __init__(self):
        if 'VCAP_SERVICES' in os.environ:
            vcap = json.loads(os.getenv('VCAP_SERVICES'))
            print('Found VCAP_SERVICES')
            if 'cloudantNoSQLDB' in vcap:
                self.creds = vcap['cloudantNoSQLDB'][0]['credentials']
                self.user = self.creds['username']
                self.password = self.creds['password']
        elif os.path.isfile('vcap-local.json'):
            with open('vcap-local.json') as f:
                vcap = json.load(f)
                print('Found local VCAP_SERVICES')
                self.creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
                self.user = self.creds['username']
                self.password = self.creds['password']

    def connect(self,name=constant.prodDb):

        self.dbName = name

        self.client = Cloudant(self.user, self.password, url='https://' + self.creds['host'], connect=True)
        self.db = self.client.create_database(self.dbName, throw_on_exists=False)


    def createNewDevice(self):
        doc = self.db.create_document({self.dataLabel : []})
        doc[self.lastUpdateLabel] = str(datetime.datetime.now())
        doc[self.commandLabel] = []
        doc.save()
        return doc["_id"]

    def addData(self,id,state, time=datetime.datetime.now()):
        doc = self.db[id]
        Document.list_field_append(doc,self.dataLabel,{
            self.timeLabel : str(time),
            self.statusLabel : state
        })
        doc[self.lastUpdateLabel] = str(time)
        doc.save()

    """
    dataArray is an array of tuple
    each tuple has in fist position the data and in second position the timestamp
    """
    def addDataArray(self,id,dataArray):
        doc = self.db[id]
        for i in dataArray:
            Document.list_field_append(doc,self.dataLabel,{
                self.timeLabel : str(i[1]),
                self.statusLabel : i[0]
            })

        doc[self.lastUpdateLabel] = str(datetime.datetime.now())
        doc.save()

    def clearDatabase(self):
        self.client.delete_database(self.dbName)
        self.db = None

    def disconnect(self):
        self.client.disconnect()
        self.client = None
        self.db = None

    def getDataFromId(self,id):
        doc = self.db[id]

        return doc[self.dataLabel]

    def getDeviceList(self):
        return self.db.keys(remote=True)

    def resetConnection(self):
        self.disconnect()
        self.connect()

    def getIdLastUpdate(self,id):
        doc = self.db[id]
        return doc[self.lastUpdateLabel]

    def addCommand(self, id, command):
        doc = self.db[id]
        doc[self.commandLabel].append(command)
        doc.save()

    def getCommandList(self, id):
        doc = self.db[id]
        return doc[self.commandLabel]

    def deleteCommands(self, id):
        doc = self.db[id]
        doc[self.commandLabel] = []
        doc.save()
