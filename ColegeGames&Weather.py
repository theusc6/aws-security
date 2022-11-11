import requests 
import os
from dotenv import load_dotenv

load_dotenv("CFBData.env")

auth_token = os.getenv('auth_token')
 
api_url1 = "https://api.collegefootballdata.com/games?year=2022"
api_url2 = "https://api.collegefootballdata.com/games/weather?year=2022"
token = {
    'Authorization': "Bearer "  + auth_token,
    'Content-Type': 'application/json'
}

response1 = requests.get(url=api_url1, headers=token)
response2 = requests.get(url=api_url2, headers=token)


print(response1.json() + response2.json())