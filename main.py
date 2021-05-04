import requests
from datetime import *
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

query = input("What did you do?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

params = {
    "query": query,
    "gender": "male",
    "weight_kg": 77.5,
    "height_cm": 175.25,
    "age": 29,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()
print(result)

todays_date = datetime.today().strftime("%m/%d/%Y")
now_time = datetime.today().strftime(("%X"))

sheety_headers = {
    "Authorization": "Bearer yummytoken"
}


for exercise in result["exercises"]:
    add_row_params = {
        "workout": {
            "date": todays_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    add_row_endpoint = "https://api.sheety.co/802ab903566d952628c23c0c93790639/myWorkouts/workouts"
    add_a_row = requests.post(url=add_row_endpoint, json=add_row_params, headers=sheety_headers)
    add_a_row.raise_for_status()

