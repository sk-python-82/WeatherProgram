# Import necessary libraries
import requests
# API key from OpenWeatherMap (replace with your own API key)
api_key = "YOUR_API_KEY"

def get_weather(city):
    """Retrieve weather data for a specified city."""
    try:
        # Create the API request URL
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        # Send a GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract relevant weather information
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]

            # Display the weather information
            print(f"Weather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Description: {description.capitalize()}")
        else:
            print("Error: Unable to retrieve weather data.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program loop
while True:
    # Get the city input from the user
    city = input("Enter the city name (or 'quit' to exit): ")

    if city.lower() == "quit":
        print("Goodbye!")
        break

    # Call the get_weather function to retrieve weather data
    get_weather(city)