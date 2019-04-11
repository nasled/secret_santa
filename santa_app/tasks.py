from celery import Celery
from django.core.mail import send_mass_mail
from django.conf import settings

# celery worker -A tasks
app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task(ignore_result=True)
def send_emails(userOne, userTwo):
    messageForUserOne = settings.EMAIL_TEMPLATE.replace('%username%', userOne.username).replace('%email%', userTwo.email)
    messageForUserTwo = settings.EMAIL_TEMPLATE.replace('%username%', userTwo.username).replace('%email%', userOne.email)

    message1 = (settings.EMAIL_SUBJECT,
                messageForUserOne,
                settings.EMAIL_FROM,
                [userOne.email])

    message2 = (settings.EMAIL_SUBJECT,
                messageForUserTwo,
                settings.EMAIL_FROM,
                [userTwo.email])
    # print(message1)
    # print(message2)

    send_mass_mail((message1, message2), fail_silently=False)



