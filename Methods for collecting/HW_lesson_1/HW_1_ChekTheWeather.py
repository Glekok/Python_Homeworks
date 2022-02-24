import requests

city = input(str("Choose your city >>> "))
API_key = ""


def coordinates(target):
    coordinates_here = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_key}"
    r = requests.get(coordinates_here).json()
    if r:
        lat_lon = [r[0]["lat"], r[0]["lon"]]
        return lat_lon
    else:
        print(f"The city - '{target}' not found!")


def temperature(target):
    try:
        lat = coordinates(city)[0]
        lon = coordinates(city)[1]
    except TypeError:
        return None
    temp_here = f"http://api.openweathermap.org/data/2.5/weather?units=metric&lat={lat}&lon={lon}&appid={API_key}"
    r = requests.get(temp_here).json()
    temp = r["main"]["temp"]
    feels = r["main"]["feels_like"]
    description = r["weather"][0]["description"]
    print(
        f"In \033[32m\033[1m'{target.upper()}'\033[38m right now: {temp}C, but feels like: {feels}C, "
        f"and {description}.")


if __name__ == "__main__":
    temperature(city)
