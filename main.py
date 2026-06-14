from fastapi import FastAPI,Depends
import json
from app.api_client import test_api


app = FastAPI()

# once user is in search they can specify the food they want with {food_id} as it takes in that parameter from api_client.py
@app.get("/home/{food_search}")
async def food_search(food_search):
   return test_api(food=food_search)
