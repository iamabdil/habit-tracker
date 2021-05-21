import requests
from datetime import datetime
import os

USERNAME = os.environ['USERNAME']
TOKEN = os.environ['TOKEN']
pixela_endpoint = os.environ['PIXELA_ENDPOINT']
GRAPH_ID = "graph78"


# CREATE A USER ACCOUNT

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)

# CREATE A GRAPH DEFINITION

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph78",
    "name": "Gym Graph",
    "unit": "Times",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# POSTING A PIXEL

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}

response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
print(response.text)