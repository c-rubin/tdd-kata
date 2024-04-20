from flask import Flask, request

import json

from auxiliary import BinListMocker, CardCounterMock

app = Flask(__name__)

api1 = '/api/card-scheme/verify/'
api2 = '/api/card-scheme/stats'

def getResponseData(cardNum):
    response = BinListMocker.getData(cardNum)
    try:
        return response
    except ValueError:
        return None
    
def getCheckedCards(start, limit):
    return CardCounterMock.getCardsChecked(start, limit)

def checkedCard(cardNum):
    CardCounterMock.checkedCard(cardNum)


@app.route(api1+"<cardNum>", methods=['GET'])
def verify(cardNum):
    response = getResponseData(cardNum)
    if response!=None:
        checkedCard(cardNum)        
        payload = {}
        payload["scheme"] = response["scheme"]
        payload["type"] = response["type"]
        payload["bank"] = response["bank"]["name"]

        return {"success":True, "payload": payload}

    return {"success":False}



@app.route(api2, methods=["GET"])
def stats():
    if len(request.args)==0: return {"success":False}
    args = request.args
    payload = getCheckedCards( int(args.get("start")), int(args.get("limit")))
    return {"success":True, "start":int(args.get("start")), "limit":int(args.get("limit")), "payload":payload}