import requests
api_key= "-"

api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=Cairo"

def fetch_data():
    print("Fetching Weather Data From WeatherStack API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response recieved successfully!")
        return response.json()

    except requests.execptions.RequestExeception as e:
        print(f"An error occured: {e}")
        raise


def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Cairo, Egypt', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Cairo', 'country': 'Egypt', 'region': 'Al Qahirah', 'lat': '30.050', 'lon': '31.250', 'timezone_id': 'Africa/Cairo', 'localtime': '2026-03-25 12:34', 'localtime_epoch': 1774442040, 'utc_offset': '2.0'}, 'current': {'observation_time': '10:34 AM', 'temperature': 16, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '05:53 AM', 'sunset': '06:09 PM', 'moonrise': '10:26 AM', 'moonset': '12:24 AM', 'moon_phase': 'First Quarter', 'moon_illumination': 41}, 'air_quality': {'co': '315.85', 'no2': '45.35', 'o3': '51', 'so2': '53.05', 'pm2_5': '29.05', 'pm10': '41.35', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 25, 'wind_degree': 235, 'wind_dir': 'SW', 'pressure': 1000, 'precip': 0.7, 'humidity': 68, 'cloudcover': 75, 'feelslike': 16, 'uv_index': 4, 'visibility': 10, 'is_day': 'yes'}}

