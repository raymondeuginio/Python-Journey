import requests
from datetime import datetime
GENDER = "male"
WEIGHT = 87
HEIGHT = 180
AGE = 18

NAPPID = "b5311118"
NAPIKEY = "d9f5f80cd6f5707d5338afcf2e396dcb"

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/c74b69a125396577c51dd00b790018d9/workoutTracking/workouts"

# -- NUTRI --
exercise_text = input("Tell me which exercises you did: ")

nutri_headers = {
    "x-app-id": NAPPID,
    "x-app-key": NAPIKEY,
}

nutri_params = {
    "query": exercise_text,
    "gender" : GENDER,
    "weight_kg": WEIGHT,
    "age": AGE,
}

response = requests.post(url=nutri_endpoint, json= nutri_params, headers=nutri_headers)
result = response.json()

# -- SHEETY --
today_date = datetime.now().strftime("%d/%m/%y")
now_time = datetime.now().strftime("%X")

heards = ["Authorization", "Basic am9oYW5uZXNrYXJsOmowaGFubmVza2FyIQ=="]

for each in result["exercises"]:
    sheet_input = {
        "workout" : {
            "date": today_date,
            "time": now_time,
            "exercise": each["name"].title(),
            "duration": each["duration_min"],
            "calories": each["nf_calories"]
        }
    }

    sheetyresponse = requests.post(
        url=sheety_endpoint, 
        json=sheet_input, 
        auth = ("johanneskarl",
                "j0hanneskar!")
        )
    print(sheetyresponse.text)

