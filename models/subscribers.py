from google.appengine.ext import ndb
from google.appengine.api import taskqueue


class Subscriber(ndb.Model):
    subscriber_email = ndb.StringProperty()
    subscriber_town = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    deleted = ndb.BooleanProperty(default=False)

    @classmethod
    def create(cls, subscriber_email, subscriber_town):
        subscriber = Subscriber(subscriber_email=subscriber_email, subscriber_town=subscriber_town)
        subscriber.put()

        #  background task for application owner for new subscriber
        taskqueue.add(url="/task/email-to-owner", params={"subscriber_email": subscriber_email, "subscriber_town": subscriber_town})

        return subscriber
