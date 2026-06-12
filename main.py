from fastapi import FastAPI,Depends

from app.api_client import test_api


app = FastAPI()



# @app.get("/user")
# async def food_search(item_id):
#     item_id = "Arrabiata"
#     return test_api(item_id)

@app.get("/user/{food_id}")
async def food_search(food_id):
   return test_api(food=food_id)
