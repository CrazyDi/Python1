import pprint
import requests
from dateutil.parser import parse


class OpenWeatherForecast:

    def __init__(self):
        self._cached_data = {}

    def get(self, city):
        if city in self._cached_data:
            return self._cached_data[city]

        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID=bf1d1da18c4b32c263a233fa7b7254d8&units=metric"
        print("sending HTTP request")
        data = requests.get(url).json()
        forecast_data = data["list"]
        forecast = []
        for day_data in forecast_data:
            count_data = 0
            for i in forecast:
                if i["date"] == parse(day_data["dt_txt"]).date():
                    if int(day_data["main"]["temp_max"]) > i["high_temp"]:
                        i.update({"high_temp": int(day_data["main"]["temp_max"])})
                    count_data = 1

            if count_data == 0:
                forecast.append({"date": parse(day_data["dt_txt"]).date(),
                                 "high_temp": int(day_data["main"]["temp_max"])})

        self._cached_data[city] = forecast
        return forecast


class CityInfo:

    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or OpenWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)

def _main():
    weather_forecast = OpenWeatherForecast()
    for i in range(5):
        city_info = CityInfo("Minsk", weather_forecast=weather_forecast)
        forecast = city_info.weather_forecast()

    pprint.pprint(forecast)

if __name__ == "__main__":
    _main()