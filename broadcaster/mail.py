from user_signup.tasks import send_parallel_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from user_signup.token import account_activation_token
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from adcbackend.secrets import EmailToken
from user_signup.models import TeacherProfile, StudentProfile


# @shared_task()
def broadcast_mail(subject, content, to_email):
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


def MailVerification(user, type):
    # domain = current_site.domain
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)

    name = user.first_name
    receiver_email = user.email
    subject = 'Verify Your Email'
    html_content = str('<h3> Hello ' + name.capitalize() + ',</h3>'
                        '<p>Please click on the link to confirm your registration,</p>'
                        'http://ec2-13-126-196-234.ap-south-1.compute.amazonaws.com/'
                       + 'user/verify_email/' + uid + '/' + token)
    broadcast_mail(subject, html_content, receiver_email)
    # send_parallel_mail.delay(subject, html_content, receiver_email)
