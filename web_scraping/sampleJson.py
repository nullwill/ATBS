import json

sample_json = """
{
  "location": {
    "name": "New York",
    "region": "NY",
    "country": "USA",
    "lat": 40.71,
    "lon": -74.01,
    "timezone_id": "America/New_York",
    "localtime": "2025-07-06 14:30"
  },
  "current": {
    "temperature": 29,
    "weather_descriptions": ["Partly cloudy"],
    "wind_speed": 13,
    "wind_degree": 230,
    "wind_dir": "SW",
    "pressure": 1012,
    "humidity": 65,
    "feelslike": 31,
    "uv_index": 6,
    "visibility": 10,
    "is_day": "yes",
    "weather_icons": [
      "https://example.com/icons/partly-cloudy.png"
    ]
  },
  "forecast": {
    "2025-07-07": {
      "maxtemp": 31,
      "mintemp": 24,
      "avgtemp": 27,
      "totalprecip": 0.2,
      "daily_will_it_rain": 1,
      "condition": "Scattered Thunderstorms"
    },
    "2025-07-08": {
      "maxtemp": 28,
      "mintemp": 22,
      "avgtemp": 25,
      "totalprecip": 1.5,
      "daily_will_it_rain": 1,
      "condition": "Rain Showers"
    }
  }
}

"""

data = json.loads(sample_json)

print(data['location'])