from handlers.base import BaseHandler
from google.appengine.api import mail


class EmailToOwnerWorker(BaseHandler):
    def post(self):
        # get email/town
        subscriber_email = self.request.get("subscriber_email")
        subscriber_town = self.request.get("subscriber_town")

        # send mail to owner for new subscriber
        mail.send_mail(sender="pavlovicbojan86@gmail.com",
                       to="pavlovicbojan86@gmail.com",
                       subject="New Subscriber today !",
                       body="""Subscriber e-mail: {0} ; Subscriber town: {1} """.format(subscriber_email,
                                                                                        subscriber_town))
