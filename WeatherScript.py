from weather import Weather, Unit
from win10toast import ToastNotifier
import time


class Main:

    def __init__(self):
        i = 0
        weather = Weather(unit=Unit.CELSIUS)
        toaster = ToastNotifier()
        while i != 1:
            location = weather.lookup_by_location('london')
            condition = location.condition
            forecasts = location.forecast
            forecast = "High:                     " + forecasts[0].high + "\nLow:                      " + forecasts[0].low + "\nDescription:           " +  forecasts[0].text
            weatherString = "Current Temp:      " + condition.temp + "\n"

            toaster.show_toast("Hanky Weather Script", weatherString + forecast, icon_path="favicon.ico", duration=15)

            hour = Hour()
            time.sleep(hour.get_wait_time())


class Hour:

    def get_wait_time(self):
        return 3600 - (int(time.time()) % 3600)


main = Main()
