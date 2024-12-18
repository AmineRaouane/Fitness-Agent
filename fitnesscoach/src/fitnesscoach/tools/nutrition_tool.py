import requests
import os

def calculate_BMI(weight_value,weight_unit,height_value,height_unit,sex,age,waist,hip) -> str:
    url = "https://bmi.p.rapidapi.com/v1/bmi"
    payload = {
    	"weight":{
            'value':weight_value,
            'unit':weight_unit
        },
    	'height':{
            'value':height_value,
            'unit':height_unit
        },
    	"sex": sex,
    	"age": age,
    	"waist": waist,
    	"hip": hip,
    }
    headers = {
    	"x-rapidapi-key": os.getenv('RAPID_API_KEY'),
    	"x-rapidapi-host": "bmi.p.rapidapi.com",
    	"Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return f"""Bmi calculated successfuly
        Results : {response.json()}"""
