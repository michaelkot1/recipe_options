import httpx


print("file is running")
base_url = "https://www.themealdb.com/api/json/v1/"
api_key = "1"

def test_api(food):
    url = f"{base_url}/{api_key}/search.php"
    params = {"s":food}

    response = httpx.get(url,params=params)
    return response.text
    # print(response.url)
    # print("status code:",response.status_code)
    # print("final url:",response.url)
    # print("response body: ",response.text[:500])

if __name__ == "__main__":
    test_api()