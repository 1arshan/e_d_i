from user_signup.tasks import send_parallel_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from user_signup.token import account_activation_token


def MailVerification(user, current_site):
    domain = current_site.domain
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)
    name = user.first_name
    receiver_email = user.email
    subject = 'Verify Your Email'
    html_content = str('<h3> Hello ' + name.capitalize() + ',</h3>'
                    '<p>Please click on the link to confirm your registration,</p>'
                    'http://' + domain + '/' + 'signup/verify_email/' + uid + '/' + token)

    send_parallel_mail.delay(subject, html_content, receiver_email)
