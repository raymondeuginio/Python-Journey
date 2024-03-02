import requests
from datetime import datetime, timedelta

API_KEY = "upeHr3oLoUA-mmrYdgCSasiqwRcRYt41"
API_ENDPOINT = "https://api.tequila.kiwi.com/search"

tommorow = datetime.now() + timedelta(days = 1)
sixmonths = tommorow + timedelta(days=44)

class FlightSearch:
#     #This class is responsible for talking to the Flight Search API.
    def __init__(self,flyto:list) -> None:
        wtg = ",".join(flyto)
        self.params = {
            "fly_from": "CGK",
            "fly_to": wtg, #flyto expecting "DPS,SIN,TYO"
            "date_from": tommorow.date(),
            "date_to": sixmonths.date(),  
            "sort":"price"
        }

        self.headers = {
            "apikey": API_KEY
        }

        response = requests.get(url=API_ENDPOINT, params=self.params, headers=self.headers)
        self.result = response.json()["data"]
        self.resultlist = []

        for each in self.result:
            resultdict = {} # ini akan di append ke resultlist
            convertedtime = datetime.fromtimestamp(each["dTime"])
            resultdict["to_city"]= each["flyTo"]
            resultdict["time"]= convertedtime.strftime("%Y-%B-%d %H:%M:%S %p")
            resultdict["unixtime"]= convertedtime
            resultdict["airlines"] = each["airlines"]
            resultdict["price"]= each["price"]
            self.resultlist.append(resultdict)
        
        