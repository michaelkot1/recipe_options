import httpx
import json

print("file is running")
base_url = "https://www.themealdb.com/api/json/v1/"
api_key = "1"

def test_api(food):
    url = f"{base_url}/{api_key}/search.php"
    params = {"s":food}

    response = httpx.get(url,params=params)
    data = response.json()

    strMeal = {}
    for i in range(0,1):
        strMeal['food_id'] = {data['meals'][i]["idMeal"]}
    return strMeal

    

    
    

    # print(response.url)
    # print("status code:",response.status_code)
    # print("final url:",response.usrl)
    # print("response body: ",response.text[:500])

if __name__ == "__main__":
    test_api()