
from django.core.mail import send_mail
from django.conf import settings

def send_application_email(recipient_email, application_id):
    subject = 'Scholarship Application Submitted'
    message = f'Your scholarship application with ID {application_id} has been successfully submitted.'
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [recipient_email],
        fail_silently=False,
    )
