testDb = 'test'
prodDb = 'iotsensor'

statusLabel = 'status'
statusOK = 'OK'
statusKO = 'KO'

idLabel = 'id'
valueLabel = 'val'
dataLabel='data'
errorLable= 'error'
commandLabel = "command"

COMMANDS = {
    "data" : [
        {
            "label" : "sleep default",
            "command" : "sleep_default"
        },
        {
            "label" : "sleep time 3000ms",
            "command" : "sleep_3000"
        },
        {
            "label" : "disable sleep",
            "command" : "nosleep"
        },
        {
            "label" : "modem sleep",
            "command" : "modemsleep"
        },
        {
            "label" : "switch to send mode",
            "command" : "switch_send"
        },
        {
            "label" : "switch to store mode",
            "command" : "switch_store"
        },
        {
            "label" : "max stored data 64",
            "command" : "max_data64"
        },
        {
            "label" : "max stored data 128",
            "command" : "max_data128"
        },
        {
            "label" : "max stored data 512",
            "command" : "max_data512"
        }
    ]
}
