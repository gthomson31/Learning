import requests
import json

if __name__ == '__main__':

    response = requests.get("http://api.open-notify.org/iss-pass.json")
    print(response.status_code)

    # Set up the parameters we want to pass to the API.
    # This is the latitude and longitude of New York City.
    parameters = {"lat": 40.71, "lon": -74 }

    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

    #print (response.content)

    # This gets the same data as the command above
    response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
    #print(response.content)


    # This gets the same data as the command above
    response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
    data = (response.json())

    # Get the response from the API endpoint.
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()

    names = []
    print (data)

    for y in (data["people"]):
        print ((y['name']))
        names.append((y['name']))




    print (names)





