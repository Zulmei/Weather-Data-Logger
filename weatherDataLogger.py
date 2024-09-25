import requests
import json

api_key = "96872ac8f3912c22bb1e394457de5f76"

def create_weather_data_url(city_name):
    return f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=96872ac8f3912c22bb1e394457de5f76"

# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def get_api_data(url):

    # Make the HTTP request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:

        # Parse the JSON response
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None

# Function to write data to text file
def write_data_to_file(data, filename):

    # Open the file in write mode
    with open(filename, 'w') as f:

        # Convert json to string and write to file
        json.dump(data, f, indent=4) # indent for readability
        print("Weather informaton send to",filename)


city_name = input("Enter the name of the city: ")

weather_data_url = create_weather_data_url(city_name)


weather_data = get_api_data(weather_data_url)
write_data_to_file(weather_data, "weather_data.txt")