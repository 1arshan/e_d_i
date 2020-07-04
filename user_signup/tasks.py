"""from celery import shared_task
from twilio.rest import Client
from adcbackend.secrets import SmsToken
from rest_framework.response import Response
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from adcbackend.secrets import EmailToken

@shared_task
def send_parallel_sms(phone_number, content):
    message_to_broadcast = content
    client = Client(SmsToken.sid_key, SmsToken.secret_key)
    phone_number = "+91" + phone_number

    try:
        client.messages.create(to=phone_number,
                               from_=SmsToken.phone_number,
                               body=message_to_broadcast)
    except Exception:
        print("otp not send")
    return Response("messages sent!", status=None)


@shared_task()
def send_parallel_mail(subject, content, to_email):
    message = Mail(
        from_email=EmailToken.from_email,
        to_emails=to_email,
        subject=subject,
        html_content=content
    )

    try:

        sg = SendGridAPIClient(EmailToken.sendgrid_token)
        response = sg.send(message)
        # print("mail send")
    except Exception as e:
        # print("mail not send")
        print(e)
"""