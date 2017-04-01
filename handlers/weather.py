from google.appengine.api import urlfetch
import json

from handlers.base import BaseHandler
from utils import secrets


class WeatherHandler(BaseHandler):
    def post(self):
        city = self.request.get("city")  # get city from user
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + secrets.secret()  # API open weather url
        content = urlfetch.fetch(url)  # convert to JSON
        result = json.loads(content.content)  # content JSON

        icon_code = result["weather"][0]["icon"] # get icon code

        icon_url = "http://openweathermap.org/img/w/" + icon_code + ".png" # icon url

        params = {"result": result, "icon_url": icon_url}

        self.render_template("result.html", params=params)


class MarsWeatherHandler(BaseHandler):
    def get(self):
        url = "http://marsweather.ingenology.com/v1/latest/"  # API for weather on MARS
        result = urlfetch.fetch(url) # convert to JSON
        podatki = json.loads(result.content)
        params = {"podatki": podatki}

        return self.render_template("mars.html", params=params)
