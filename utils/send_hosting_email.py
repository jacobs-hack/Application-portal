import sendgrid
import os
from sendgrid.helpers.mail import *

_SENDER = "applications@jacobshack.com"
_SUBJECT = "Hosting fellow hackers for jacobsHack! Fall 2016"
_EMAIL_BODY = """Hello {},\n
You are getting this email because you have been accepted to jacobsHack! Fall 2016 that is happening on 15th - 16th October at Jacobs University in Bremen, Germany.

If you are travelling from outside Bremen, arriving on Friday, and need a place to crash, please fill out our guest matching form: https://jacobshack.typeform.com/to/cf5yLu.

We will try our best to match you with students but since there are only few hosts because it's a small university, we also recommend looking at nearby hostels www.hostelworld.com/Hostels/Bremen.

If you are from Bremen and are willing to host a student, please fill out the student matching form https://jacobshack.typeform.com/to/fSUW5X

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

    apps_to_email = JHAPP.apps.get_accepted()
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
