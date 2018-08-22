from random import random
from json import dumps
import requests

def populate():
    #Id to populate
    id = "34560ab9bcc71380f9ba49566b93b0a0"
    #How many entries to create
    n = 100
    arr = []
    for i in range(n):
        state = 0
        if random() > 0.5:
            state = 1
        arr.append(state)
    request = {
        "id" : id,
        "val" : arr
    }
    contents = requests.post("http://127.0.0.1:8001/device/measure", data=dumps(request))
    return print(contents)
    
        


populate()