from handlers.base import BaseHandler
from models.subscribers import Subscriber


class SubscribeHandler(BaseHandler):
    def get(self):
        return self.render_template("subscribe.html")

    def post(self):

        # get subscribers mail/town
        subscriber_email = self.request.get("subscriber_email")
        subscriber_town = self.request.get("subscriber_town")

        # put email/town in Datastore
        Subscriber.create(subscriber_email=subscriber_email, subscriber_town=subscriber_town)

        return self.redirect_to("main-page")
