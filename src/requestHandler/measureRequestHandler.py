import requestHandler.handler as handler
import datetime

class MeasureRequestHandler(handler.RequestHandler):

    def handle(self,request):
        resp = super(MeasureRequestHandler, self).handle(request)
        info = self.parser.getMeasureInfo(request.data)
        id = info[0]
        data = info[1]
        try:
            lastUpdate = datetime.datetime.strptime(self.db.getIdLastUpdate(id),"%Y-%m-%d %H:%M:%S.%f")
        except KeyError:
            resp.data = self.parser.unknownIdError()
            return resp

        timeDelta = (datetime.datetime.now() - lastUpdate) / len(data)

        dataArray = []
        for i in range(len(data)):
            time = lastUpdate+timeDelta * (i+1)
            dataArray.append((data[i],time))

        self.db.addDataArray(id,dataArray)
        commandList = self.db.getCommandList(id)
        resp.data = self.parser.measureResponse(commandList)
        self.db.deleteCommands(id)
        return resp
