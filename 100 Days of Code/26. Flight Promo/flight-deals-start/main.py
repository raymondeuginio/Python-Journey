#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

my_gmail = "johanneskarl50@gmail.com"
password = "ampl nlkf oygp fbgf"

dmanager = DataManager()
fsearch = FlightSearch(dmanager.city)
fdata = FlightData(fsearch.resultlist, dmanager.result)

if fdata.searchcheapest():
    notif = NotificationManager(my_gmail,password)
    notif.convertmsg(fdata.murmer)
else:
    print("There's no promo-promo")