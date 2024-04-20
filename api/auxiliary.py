import requests

class BinListMocker:
    bin = ['45717360','45717361','45717362','45717363','45717364'] #all these BINs have the same response from https://lookup.binlist.net/
    api = 'https://lookup.binlist.net/'
    mock = True
    response = {"number":{},"scheme":"visa","type":"debit","brand":"Visa Classic","country":{"numeric":"208","alpha2":"DK","name":"Denmark","emoji":"🇩🇰","currency":"DKK","latitude":56,"longitude":10},"bank":{"name":"Jyske Bank A/S"}}
    
    def getData(bin):
        if BinListMocker.mock:
            if bin in BinListMocker.bin: return BinListMocker.response
            return ""
        return BinListMocker.getRealData(bin)

    def getRealData(bin):
        response = requests.get(BinListMocker.api+bin)
        return response.text
    
class CardCounterMock:
    mock = True
    cardsChecked = {}

    def checkedCard(cardNum):
        if cardNum in CardCounterMock.cardsChecked: CardCounterMock.cardsChecked[cardNum]+=1
        else: CardCounterMock.cardsChecked[cardNum] = 1

    def getCardsChecked(start, limit):
        i=1
        response = {}
        for x in CardCounterMock.cardsChecked:
            if i>limit: break
            if i<start: continue
            response[x] = CardCounterMock.cardsChecked[x]
            i+=1
        return response
