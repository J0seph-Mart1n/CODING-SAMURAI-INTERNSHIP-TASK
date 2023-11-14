import requests

api_key = open('api.txt', 'r').read()   #Give your own API

user_input_city = input("Enter city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?"
weather_data = requests.get(f"{base_url}q={user_input_city}&units=imperial&APPID={api_key}")

#Function is used to get all the weather information of the city
def get_weather_data(user_input_city, unit="metric"):
    if weather_data.status_code == 200:     #Error Handling (if the city exists status_code returns 200)
        data = weather_data.json()
        return data
    else:
        return None

#Function displays the weather information of the city
def display_weather_info(data, unit):

    if data is None:
        print("City does not exists!!")
        return 0

    if unit == 'fahrenheit' :
        temperature = data['main']['temp']
        unit_symbol = '°F'
    else:
        temperature = (data['main']['temp'] - 32) * 5/9          #Converting Fahrenheit to Celsius 
        unit_symbol = '°C'

    if data is not None:
        print("\nWeather Information for", data["name"], ",", data["sys"]["country"])
        print("Temperature of city:", temperature, unit_symbol)
        print("Humidity of city:", data["main"]["humidity"], "%")
        print("Wind Speed of city:", data["wind"]["speed"], "m/s")
        print("Weather Conditions of city:", data["weather"][0]["description"])

#Main function 
def main():
    print("Weather Forecast for Today")
    unit = input("Choose a temperature unit (Celsius or Fahrenheit): ").lower()

    if unit not in ["celsius", "fahrenheit"]:
        print("Invalid choice. Switching to Celsius.")
        unit = "celsius"

    data = get_weather_data(user_input_city)

    display_weather_info(data, unit)

if __name__ == "__main__":
    main()