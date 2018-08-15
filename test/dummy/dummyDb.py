import datetime

dummyId = "hello"

class DummyDB:

    def connect(self,name):
        pass

    def createNewDevice(self):
        return dummyId

    def addData(self,dat1,dat2,time=datetime.datetime.now()):
        pass

    def getIdLastUpdate(self,id):
        return str(datetime.datetime.now())

    def getCommandList(self,id):
        return []

    def deleteCommands(self,id):
        return

    def addDataArray(self,id,dataArray):
        pass
