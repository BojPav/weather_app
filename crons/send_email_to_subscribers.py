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
            current_temp = result["main"]["temp"]
            wind_speed = result["wind"]["speed"]
            humidity = result["main"]["humidity"]
            description = result["weather"][0]["description"]
            pressure = result["main"]["pressure"]
            mail.send_mail(sender="pavlovicbojan86@gmail.com",
                           to=subscriber.subscriber_email,
                           subject="Weather info in your town: %s" % subscriber.subscriber_town,
                           body="""Current Temperature: {0} C ; \n
                           Wind speed: {1} km/h; \n
                           Humidity: {2} %; \n
                           Description: {3} ; \n
                           Pressure: {4} mBar""".format(current_temp, wind_speed, humidity, description, pressure))
