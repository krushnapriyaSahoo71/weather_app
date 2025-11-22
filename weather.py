import requests

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            print("❌ City not found. Please try again.")
            return None

        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"].title()
        }

        return weather

    except:
        print("⚠ Error: Unable to fetch weather data.")
        return None


def display_weather(info):
    print("\n------ Weather Report ------")
    print(f"🌍 City: {info['city']}")
    print(f"🌡 Temperature: {info['temperature']}°C")
    print(f"💧 Humidity: {info['humidity']}%")
    print(f"💨 Wind Speed: {info['wind_speed']} m/s")
    print(f"🌦 Description: {info['description']}")
    print("-----------------------------\n")


def main():
    print("=== Weather App using Python ===")
    city = input("Enter city name: ")
    result = get_weather(city)

    if result:
        display_weather(result)


if __name__ == "__main__":
    main()
