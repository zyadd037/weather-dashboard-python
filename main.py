from weather import get_weather


def display_weather(data):

    city_name = data["location"]["name"]
    country_name = data["location"]["country"]

    temperature = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    wind_speed = data["current"]["wind_kph"]

    condition = data["current"]["condition"]["text"]

    print("\n========================================")
    print("           WEATHER DASHBOARD")
    print("========================================")

    print(f"City: {city_name}")
    print(f"Country: {country_name}")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} km/h")
    print(f"Condition: {condition}")

    print("========================================")


city = input("Enter city name: ")

data = get_weather(city)

if data is not None:
    display_weather(data)
