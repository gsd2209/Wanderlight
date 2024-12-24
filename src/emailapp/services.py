from celery import shared_task
from django.core.mail import send_mail

<<<<<<< HEAD

@shared_task
def send_email_task(
    subject,
    message,
    recipient_email,
):
=======
@shared_task

def send_email_task(subject,message,recipient_email):
>>>>>>> 6472ae2acf6526a1fb1173eadcbb7c15ed4b071a
    try:
        send_mail(
            subject=subject,
            message=message,
<<<<<<< HEAD
            from_email="khanarfa8879@gmail.com",
            recipient_list=[recipient_email],
        )
        return f"Email sent to {recipient_email}"
    except Exception as e:
        return str(e)
=======
            from_email='your_email@gmail.com',
            recipient_list=[recipient_email],

        )
        return f'Email send to {recipient_email}'
    except Exception as e:
        return str(e)
>>>>>>> 6472ae2acf6526a1fb1173eadcbb7c15ed4b071a
