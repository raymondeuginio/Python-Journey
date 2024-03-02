import requests
from datetime import datetime
# https://pixe.la/@johanneskarl
USERNAME = "johanneskarl"
TOKEN = "halimakarl555600304909"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params) 
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "Coding Minutes",
#     "unit": "minute",
#     "type": "int",
#     "color": "kuro"
# }

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "300",
}
# response = requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
# print(response.text)