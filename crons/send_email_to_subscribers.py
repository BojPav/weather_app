from google.appengine.api import mail
from google.appengine.api import urlfetch
from handlers.base import BaseHandler
from models.subscribers import Subscriber
from utils import secrets
import json


class SubscribersWeatherCron(BaseHandler):
    def get(self):

        # get weather for subscribed cities
        subscribers = Subscriber.query(Subscriber.deleted == False).fetch()
        # fetched_subscribers_emails = subscribers.subscriber_email

        # subscribers cities
        #fetched_subscribers_town = subscribers.subscriber_town

        for subscriber in subscribers:
            #city = fetched_subscribers_town  # get user city from Datastore
            url = "http://api.openweathermap.org/data/2.5/weather?q=" + subscriber.subscriber_town + "&units=metric&appid=" + secrets.secret()  # API open weather url
            content = urlfetch.fetch(url)  # convert to JSON
            result = json.loads(content.content)  # content JSON
            icon_code = result["weather"][0]["icon"]
            icon_url = "http://openweathermap.org/img/w/" + icon_code + ".png"
            current_temp = result["main"]["temp"]
            min_temp = result["main"]["temp_min"]
            max_temp = result["main"]["temp_max"]
            wind_speed = result["wind"]["speed"]
            humidity = result["main"]["humidity"]
            description = result["weather"][0]["description"]
            pressure = result["main"]["pressure"]
            mail.send_mail(sender="pavlovicbojan86@gmail.com",
                           to=subscriber.subscriber_email,
                           subject="Weather info in your town: %s" % subscriber.subscriber_town,
                           body="""Description: {0} \n
                                   Current temperature: {1} C \n
                                   Minimum temperature: {2} C \n
                                   Maximum temperature: {3} C \n
                                   Wind speed: {4} km/h \n
                                   Humidity: {5} % \n
                                   Pressure: {6} mBar""".format(description, current_temp, min_temp, max_temp, wind_speed, humidity,  pressure))
