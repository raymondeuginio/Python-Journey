import requests


API_ENDPOINT = "https://api.sheety.co/eea30a038eafac6ca8f7241676e227e7/promoTerbang/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) :
        response = requests.get(url=API_ENDPOINT)
        self.result = response.json()['prices']
        self.city = [item['iataCode'] for item in self.result]



