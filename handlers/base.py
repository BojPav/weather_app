import os
import jinja2
import webapp2
from google.appengine.api import urlfetch
import json
from utils import secrets

template_dir = os.path.join(os.path.dirname(__file__), "../templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}

        #   cookies
        cookie = self.request.cookies.get("weatherapp-cookie")

        if cookie:
            params["cookies"] = True

        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("main.html")


class AboutHandler(BaseHandler):
    def get(self):
        return self.render_template("about.html")


class CookieHandler(BaseHandler):
    def post(self):
        self.response.set_cookie(key="weatherapp-cookie", value="accepted")
        return self.redirect_to("main-page")


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
