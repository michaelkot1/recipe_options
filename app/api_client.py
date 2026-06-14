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
    
    # can try to count the amount of recipe ids there are then make that the count max?

    print(data['meals'][0])
    # ids = []4
    # counter_on = True
    # while counter_on:
    #     count = 0
    #     ids.append(data["meals"][count]["idMeal"])
    #     count += 1
    #     if count == 5:
    #         return ids

    # return ids
        
    # while data["meals"][0]["idMeal"] in 
    # for i in range(4):
    #    new.append({"recipe_info":
    #                     {"id":data["meals"][i]['idMeal'],
    #                     "name":data["meals"][i]['strMeal'],
    #                     "categroy":data["meals"][i]['strCategory'],
    #                     "cusineArea":data["meals"][i]['strArea'],
    #                     "country":data["meals"][i]['strCountry'],
    #                     "tags":data["meals"][i]['strTags']},
    #                     "links":
    #                     {"thumbnail":data["meals"][i]["strMealThumb"],
    #                      "youtube":data["meals"][i]["strYoutube"],
    #                      "sourceRecipe":data["meals"][i]["strSource"]}})


    return data

    # strMeal = {}
    # for i in range(0,1):
    #     strMeal['food_id'] = {data['meals'][i]["idMeal"]}
    # return strMeal

    

    
    

    # print(response.url)
    # print("status code:",response.status_code)
    # print("final url:",response.usrl)
    # print("response body: ",response.text[:500])

if __name__ == "__main__":
    test_api(food='pizza')