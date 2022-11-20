
import requests 
import os
import json
from dotenv import load_dotenv
import pandas as pd

load_dotenv("CFBData.env")

auth_token = os.getenv('auth_token')
 
api_urls = ["https://api.collegefootballdata.com/games?year=2022", "https://api.collegefootballdata.com/games/weather?year=2022",
"https://api.collegefootballdata.com/lines?year=2022"]

token = {
    'Authorization': "Bearer "  + auth_token,
    'Content-Type': 'application/json'
}

number = 1

while number < 4:
    for api_url in api_urls:
        response = requests.get(url=api_url, headers=token)
        response_dict = response.json()
        pretty = json.dumps(response_dict, indent=4)

        with open(f'{number}.data.json', 'w') as json_file:
            json_file.write(pretty)

        number += 1