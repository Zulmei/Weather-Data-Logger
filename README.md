# Weather Data Logger

A Python application that retrieves real-time weather data using the OpenWeather API and stores it in a JSON format text file. The program also allows the user to read and parse this data, displaying key weather information such as temperature, humidity, and weather description.

## Features

- Fetches real-time weather data for a specified city using the OpenWeather API.
- Stores the weather information in a JSON file (`weather_data.txt`).
- Reads and parses the JSON file to display the city name, temperature, humidity, and weather conditions.
- Easy-to-use input system for selecting the city to fetch data for.

## Files

- **weatherDataLogger.py**: Contains the main functionality for fetching and storing weather data.
- **usingWeatherData.py**: Reads and parses the JSON file to display the weather data.
- **weather_data.txt**: Example output file storing weather information for the city

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Zulmei/Weather-Data-Logger.git
   ```
2. Install the required libraries (if not installed):
   ```bash
   pip install requests
   ```
3. To fetch and store weather data:
   - Run weatherDataLogger.py:
   ```bash
   python weatherDataLogger.py
   ```
4. To read and display stored weather data:
   - Run usingWeatherData.py:
   ```bash
   python usingWeatherData.py
   ```

## Technologies Used

- Python
- API Integration: OpenWeather API
- JSON: For storing and reading weather data
