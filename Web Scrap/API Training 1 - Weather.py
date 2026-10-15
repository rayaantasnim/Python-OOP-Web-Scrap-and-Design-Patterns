import requests
api_key = "d3e32d448f57160e352fefe7e60766e9"

def get_weather(city_name):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(api_url)
    print(response.status_code)
    data = response.json()
    
    temp = data["main"]["temp"]
    max_temp = data["main"]["temp_max"]
    min_temp = data["main"]["temp_min"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"]["deg"]
    weather_desc = data["weather"][0]["description"]
    country = data["sys"]["country"]
    sunrise = data["sys"]["sunrise"]
    sunset = data["sys"]["sunset"]
    
    print(f"Temperature: {temp}°C")
    print(f"Max Temperature: {max_temp}°C")
    print(f"Min Temperature: {min_temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Wind Direction: {wind_deg}°")
    print(f"Weather Description: {weather_desc}")
    print(f"Country: {country}")
    print(f"Sunrise (Unix): {sunrise}")
    print(f"Sunset (Unix): {sunset}")


    search_field = input("\nEnter a field to search again (e.g. temp, humidity, pressure): ").strip().lower()
    if search_field == "temp" or search_field == "temperature":
        print(f"Search Result → Temperature: {temp}°C")

    elif search_field == "humidity":
        print(f"Search Result → Humidity: {humidity}%")

    elif search_field == "pressure":
        print(f"Search Result → Pressure: {pressure} hPa")

    elif search_field == "wind":
        print(f"Search Result → Wind Speed: {wind_speed} m/s, Direction: {wind_deg}°")

    elif search_field == "description":
        print(f"Search Result → Weather Description: {weather_desc}")

    elif search_field == "country":
        print(f"Search Result → Country: {country}")

    elif search_field == "sunrise":
        print(f"Search Result → Sunrise (Unix): {sunrise}")

    elif search_field == "sunset":
        print(f"Search Result → Sunset (Unix): {sunset}")

    else:
        print("Search Result → Field not found!")

a = input("Enter the city name: ").strip()
get_weather(a)