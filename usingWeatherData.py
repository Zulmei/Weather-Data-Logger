import json

# Function to read response from text file and parse as dictionary
def read_data_from_file(filename):

    # Open the file in read mode
    with open(filename, "r") as f:

        # Read the file content
        data = json.load(f)
        return data

# Example usage
weather_data = read_data_from_file('weather_data.txt')

# Print all the fields from the dictionary
print("City:", weather_data["name"])
print("Weather:", weather_data["weather"][0]["description"])
print("Temperature:", weather_data["main"]["temp"], "K")
print("Humidity:", weather_data["main"]["humidity"])

