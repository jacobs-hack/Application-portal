import sendgrid
import os
from sendgrid.helpers.mail import *

_SENDER = "applications@jacobshack.com"
_SUBJECT = "Slack Invite for jacobsHack! Fall 2016"
_EMAIL_BODY = """Hello {},\n
You are getting this email because you have been accepted to jacobsHack! Fall 2016 that is happening on 15th - 16th October at Jacobs University in Bremen, Germany.

We will be using Slack as our primary mode of communication before, during, and after the event. Please join our Slack team at https://jacobshack.skillflow.io/ to talk with other hackers and mentors attending the event.

We would like you to let us know if you can make it to the event or not. If you haven't done so already, please RSVP: https://jacobshack.typeform.com/to/b8Lagp You can also join the event on facebook for more updates https://www.facebook.com/events/277473712613843/

Event Schedule: Registration opens at 9 AM on 15th October (Saturday) and the opening ceremony starts at 10.30 AM. A more detailed schedule can be found on https://2016f.jacobshack.com/#schedule

If you have any questions, feel free to Email us at hello@jacobshack.com or message us on Facebook and Twitter.

Looking forward to see you in Bremen!

Cheers,\n
The jacobsHack! team"""
_SENDGRID = sendgrid.SendGridAPIClient(apikey="SENDGRID_API_KEY")


def email_body(recepient_name):
    return _EMAIL_BODY.format(recepient_name)


def send_email(sender, recepient, recepient_name):
    mail = Mail(sender, _SUBJECT, recepient, Content("text/plain", _EMAIL_BODY.format(recepient_name)))
    resoponse = _SENDGRID.client.mail.send.post(request_body=mail.get())
    return resoponse


if __name__ == '__main__':
    import os

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeform_viz.settings")

    import django

    django.setup()

    from hacker.models import JHAPP

    apps_to_email = JHAPP.apps.get_accepted_but_not_slacked()
    for app in apps_to_email:
        try:
            resoponse = send_email(Email(_SENDER), Email(app.email), app.first_name)
            if resoponse._status_code == 202:
                print("Sent email to {}".format(app.email))
                app.slack_invite = True
            else:
                app.slack_invite = False
                print("Can't send email to {}".format(app.email))
            app.save()
        except:
            app.slack_invite = False
            print("Can't send email to {}".format(app.email))
            app.save()
