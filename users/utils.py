from django.core.mail import EmailMessage
from django.template.loader import get_template

    
class Util:
    @staticmethod
    def send_email(data):
        email=EmailMessage(subject=data['email_subject'], body=data['email_body'], from_email='sampsontioluwanimi@gmail.com', to=[data['to_email']])
        email.send()
        

class RecruiterUtil:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email.send()
