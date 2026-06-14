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

    # food_information = {"recipe_id": {"id"}}
    food_information = {"recipe_info":{"id":int,"name":str,"categroy":str,"cusineArea":str,"country":str,"tags":list[str]},
                        "ingredients":[{ "item": str, "measurement": str }],
                        "instructions":str,"links":
                        {"thumbnail":str,"youtube":str,"sourceRecipe":str}}
    
    


    food_information["recipe_info"]["id"] = data["meals"][0]['idMeal']

    return food_information

    {
  "recipeInfo": {
    "id": "52819",
    "name": "Cajun spiced fish tacos",
    "category": "Seafood",
    "cuisineArea": "Mexican",
    "country": "Mexico",
    "tags": ["Spicy", "Fish"]
  },
  "ingredients": [
    { "item": "cajun", "measurement": "2 tbsp" },
    { "item": "cayenne pepper", "measurement": "1 tsp" },
    { "item": "white fish", "measurement": "4 fillets" },
    { "item": "vegetable oil", "measurement": "1 tsp" },
    { "item": "flour tortilla", "measurement": "8" },
    { "item": "avocado", "measurement": "1 sliced" },
    { "item": "little gem lettuce", "measurement": "2 shredded" },
    { "item": "Spring Onions", "measurement": "4 shredded" },
    { "item": "salsa", "measurement": "1 x 300ml" },
    { "item": "sour cream", "measurement": "1 pot" },
    { "item": "lemon", "measurement": "1" },
    { "item": "garlic", "measurement": "1 clove finely chopped" }
  ],
  "instructions": "Cooking in a cajun spice and cayenne pepper marinade makes this fish super succulent and flavoursome. Top with a zesty dressing and serve in a tortilla for a quick, fuss-free main that's delightfully summery.\r\n\r\nOn a large plate, mix the cajun spice and cayenne pepper with a little seasoning and use to coat the fish all over.\r\n\r\nHeat a little oil in a frying pan, add in the fish and cook over a medium heat until golden. Reduce the heat and continue frying until the fish is cooked through, about 10 minutes. Cook in batches if you don’t have enough room in the pan.\r\n\r\nMeanwhile, prepare the dressing by combining all the ingredients with a little seasoning.\r\nSoften the tortillas by heating in the microwave for 5-10 seconds. Pile high with the avocado, lettuce and spring onion, add a spoonful of salsa, top with large flakes of fish and drizzle over the dressing.",
  "links": {
    "thumbnail": "https://www.themealdb.com/images/media/meals/uvuyxu1503067369.jpg",
    "youtube": "https://www.youtube.com/watch?v=N4EdUt0Ou48",
    "sourceRecipe": "https://realfood.tesco.com/recipes/cajun-spiced-fish-tacos.html"
  }
}
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