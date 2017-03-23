#!/usr/bin/env python
import webapp2

from crons.send_email_to_subscribers import SubscribersWeatherCron
from handlers.base import MainHandler, AboutHandler, CookieHandler
from handlers.subscribe import SubscribeHandler
from handlers.weather import WeatherHandler, MarsWeatherHandler
from workers.owner_new_subscribers import EmailToOwnerWorker

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/about', AboutHandler, name="about-page"),
    webapp2.Route('/set-cookie', CookieHandler, name="set-cookie"),

    # weather
    webapp2.Route('/result', WeatherHandler, name="result"),
    webapp2.Route('/weather-mars', MarsWeatherHandler, name="weather-mars"),

    # subscribe
    webapp2.Route('/subscribe', SubscribeHandler, name="subscribe"),

    # workers
    webapp2.Route('/task/email-to-owner', EmailToOwnerWorker, name="email-to-owner"),

    # CRON jobs
    webapp2.Route("/cron/send-weather-info", SubscribersWeatherCron, name="cron-send-weather-info")
], debug=True)
