from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_task(
    subject,
    message,
    recipient_email,
):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email="khanarfa8879@gmail.com",
            recipient_list=[recipient_email],
        )
        return f"Email sent to {recipient_email}"
    except Exception as e:
        return str(e)
