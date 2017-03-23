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
        params = {"result": result}

        self.render_template("result.html", params=params)


class MarsWeatherHandler(BaseHandler):
    def get(self):
        url = "http://marsweather.ingenology.com/v1/latest/"  # API for weather on MARS
        result = urlfetch.fetch(url)
        podatki = json.loads(result.content)
        params = {"podatki": podatki}

        return self.render_template("mars.html", params=params)
