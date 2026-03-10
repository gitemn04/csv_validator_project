import requests

def generate_uuid():

    url = "https://www.uuidtools.com/api/generate/v1"

    response = requests.get(url)

    if response.status_code == 200:
        uuid_value = response.json()[0]
        print("Generated UUID:", uuid_value)
        return uuid_value
    else:
        print("API request failed")

generate_uuid()