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
            self.setContent(self.parser.unknownIdError())
            return resp

        timeDelta = (datetime.datetime.now() - lastUpdate) / len(data)

        dataArray = []
        for i in range(len(data)):
            time = lastUpdate+timeDelta * (i+1)
            dataArray.append((data[i],time))

        self.db.addDataArray(id,dataArray)


        commandList = self.db.getCommandList(id)
        self.setContent(self.parser.measureResponse(commandList))
        self.db.deleteCommands(id)

        self.db.computeOccupancy(1, 2, 2, id)

        return resp
