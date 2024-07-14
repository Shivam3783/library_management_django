from django.core.mail import send_mail
from twilio.rest import Client
from django.conf import settings

def send_notification(to_email, subject, message, to_phone=None):
    # Send email
    send_mail(subject, message, settings.EMAIL_HOST_USER, [to_email])

    # Send SMS
    if to_phone:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to_phone
        )
