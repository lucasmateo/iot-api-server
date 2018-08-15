# occupancy sensor REST api

currently hosted on : IOT-api-occupancy.eu-gb.mybluemix.net

## API
### GET /device/id

return the id associated to the device
each id is unique and specific to the requesting device that is one of the
reason the device cannot choose his own id
this id will need to be provided on future request in order to be identified

the reply should contain two entry
"status" is a string indicating if the request is accepted or not.
One of the reason a request can be rejected is that it is the right device
the server should then check that the request header "User-Agent" is correct
the only supported User-agent is "esp-idf/1.0 esp32" for now.
"status" can have two string values "OK" or "KO"

"id" is a string containing the id associated to the device
it can be missing if the status is "KO"

example of reply body :
```json
{"status": "OK","id": "qwedfgt"}
```
```json
{"status": "KO"}
```

### POST /device/measure

the device should send his data to this path. The request body should contain the
id and the value to be posted.
The "val" entry is a boolean or an array of boolean.
For now their is no time stamp and the time of the mesure is assumed to be the
same as the time at which the request is received.
In case "val" is an array, an interval will also be specified in order for the server
to be able to analyze the data. The starting time will be the one when the server
received the data.
The "inter" entry is an integer and is expressed in second

example :
```json
{"id": "qwedfgt", "val":false}
```
```json
{"id": "qwedfgt", "val":true}
```
```json
{"id": "qwedfgt", "val":[true,false,false,true,false],"inter":30}
```

For this example, if the server receive it at 14:00:00, it would interpret the
data like so :  
at 14:00:00 the device is active  
at 14:00:30 the device is inactive  
at 14:01:00 the device is inactive  
at 14:01:30 the device is active  
at 14:02:00 the device is active  


The server reply is also important and to be analyzed by the device as it can contain
command to be executed by the device.
it will contain the name of command to be executed and additional parameters

example :
```json

{
  "status" : "OK",
  "data" :
  [
    {
      "comm":"cacheData",
      "addPara":
        {
          "frq":30,"send":7200
        }
    }
  ]
}
```

### GET /api/device_list

return a list of all device id

```json
{
  "status" : "OK",
  "data" :
    [
      "4e7bb1ef1ec0fa6fc4e7e737a0cb6522",
      "4e819d8c7c75c050619ebc8631df148c",
      "da0279561413e792fe93641e922a1df7"
    ]
}
```

### GET /api/device_data/<id\>

return the data for a specified device. <id> being the string containing the id of the device

```json
{
  "status" : "OK",
  "data" :
  [
      {
          "stamp": "2018-08-02 11:43:37.145757",
          "state": "true"
      },
      {
          "stamp": "2018-08-02 11:43:38.009736",
          "state": "true"
      },
      {
          "stamp": "2018-08-02 11:43:38.873293",
          "state": "true"
      }
  ]
}

```

### error

in case of error the value of "status" will be "KO" and their will be no "data" key but a "error" key containing a string describing the cause of the error

```json
{
  "status" : "KO",
  "error" : "unknown id"
}
```
