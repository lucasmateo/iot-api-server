import json
import constant

class JsonParser:

    """
    return the content of the id response in JSON
    two entries:
        "status" can be "OK" or "KO"
        "id" is the value of the id given in response
    """
    def idResponse(self,status,id):
        stat = (constant.statusOK if status else constant.statusKO)
        return json.dumps({constant.statusLabel:stat, constant.idLabel:id})

    """
    return a tuple with in first position the id found in the string and in
    second position the value found in the string
    """
    def getMeasureInfo(self,string):
        js = json.loads(string)
        value = []
        data = js[constant.valueLabel]
        if isinstance(data,list):
            value = self.convertDataArray(data)
        else:
            if data == 1:
                value.append(True)
            else:
                value.append(False)
        return (js[constant.idLabel],value)

    def measureResponse(self, commandList):
        data = {constant.statusLabel : constant.statusOK}

        data[constant.commandLabel] = commandList
        return json.dumps(data)

    def dataResponse(self,list):
        data = {}
        data[constant.statusLabel] = constant.statusOK
        data[constant.dataLabel] = list
        return json.dumps(data)

    def listResponse(self,list):
        data = {}
        data[constant.statusLabel] = constant.statusOK
        data[constant.dataLabel] = list
        return json.dumps(data)

    def unknownIdError(self):
        data = {}
        data[constant.statusLabel] = constant.statusKO
        data[constant.errorLable] = 'unknown id'
        return json.dumps(data)

    def getData(self,string):
        data = json.loads(string)
        return data[constant.dataLabel]

    def convertDataArray(self,arr):
        res = []
        for i in arr:
            if i == 1:
                res.append(True)
            else:
                res.append(False)
        return res
