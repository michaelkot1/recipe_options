from fastapi import FastAPI,Depends
import json
from app.api_client import test_api


app = FastAPI()
@app.get("/user/{food_id}")
async def food_search(food_id):
   return test_api(food=food_id)
