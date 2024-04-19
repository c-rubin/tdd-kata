import requests

class BinListMocker:
    bin = '45717360'
    api = 'https://lookup.binlist.net/45717360'
    mock = True
    response = '{"number":{},"scheme":"visa","type":"debit","brand":"Visa Classic","country":{"numeric":"208","alpha2":"DK","name":"Denmark","emoji":"🇩🇰","currency":"DKK","latitude":56,"longitude":10},"bank":{"name":"Jyske Bank A/S"}}'
    
    def getData(bin):
        if BinListMocker.mock:
            if bin == BinListMocker.bin: return BinListMocker.response
            return ""
        return BinListMocker.getRealData(bin)

    def getRealData(bin):
        response = requests.get(BinListMocker.api)
        return response.text
