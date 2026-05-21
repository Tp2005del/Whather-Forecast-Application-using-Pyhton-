import request

api_key = "abcd1234xyz56789"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] != "404":

    main = data["main"]
    weather = data["weather"][0]
    wind = data["wind"]

    temperature = main["temp"]
    humidity = main["humidity"]
    description = weather["description"]
    wind_speed = wind["speed"]

    print("\nWeather Report")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Weather:", description)
    print("Wind Speed:", wind_speed, "m/s")

else:
    print("City not found")