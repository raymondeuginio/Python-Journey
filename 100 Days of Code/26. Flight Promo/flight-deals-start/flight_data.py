class FlightData:
   
    def __init__(self, existticket:list, wantedticket:list):
        self.exist = existticket
        self.wanted = wantedticket


    def searchcheapest(self):
        self.murmer = []
        for each in self.exist:
            self.murmerdict = []
            for city in self.wanted:
                if each['to_city'] in city['iataCode'] :
                    if each["price"] < city["lowestPrice"]:
                        self.murmerdict.append(each['to_city'],each['time'],each['airlines'],each["price"])
        if len(self.murmer) != 0:
            return self.murmer
        else:
            return False
       
   
# [{'to_country': 'Denpasar', 
#     'time': '2024-January-28 22:00:00 PM', 
#     'unixtime': datetime.datetime(2024, 1, 28, 22, 0), 
#     'airlines': ['QZ'], 'price': 45}, 
#   {'to_country': 'Denpasar', 
#    'time': '2024-January-30 22:00:00 PM', 
#    'unixtime': datetime.datetime(2024, 1, 30, 22, 0), 
#    'airlines': ['QZ'], 'price': 45}, 
#    {'to_country': 'Denpasar', 
#     'time': '2024-January-22 22:00:00 PM', 
#     'unixtime': datetime.datetime(2024, 1, 22, 22, 0), 
#     'airlines': ['QZ'], 'price': 45}]
   
