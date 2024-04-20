from flask import Flask

import json

from auxiliary import BinListMocker

app = Flask(__name__)

api1 = '/api/card-scheme/verify/'
api2 = '/api/card-scheme/stats'

def getResponseData(cardNum):
    response = BinListMocker.getData(cardNum)
    try:
        return json.loads(response)
    except ValueError:
        return None
    


@app.route(api1+"<cardNum>", methods=['GET'])
def verify(cardNum):
    response = getResponseData(cardNum)
    if response!=None:        
        payload = {}
        payload["scheme"] = response["scheme"]
        payload["type"] = response["type"]
        payload["bank"] = response["bank"]["name"]

        return {"success":True, "payload": payload}

    return {"success":False}



@app.route(api2, methods=["GET"])
def stats():
    return "{}"