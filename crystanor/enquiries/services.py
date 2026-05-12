from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives
from enquiries.models import Enquiry
from enquiries.constants import (USER_EMAIL_CONTENT, ADMIN_EMAIL_CONTENT, USER_CONFIRMATION_SUBJECT, 
                                FAIL_TO_SEND_ADMIN_NOTIFICATION, FAIL_TO_SEND_USER_NOTIFICATION, ADMIN_MAIL_SUBJECT)
from crystanor.settings import DEFAULT_FROM_EMAIL, ADMIN_EMAIL
from django.utils.html import strip_tags

class EmailService:

    def __init__(self, enquiry: Enquiry):
        self.enquiry = enquiry

    def send_admin_notification(self):
        """
        Send enquiry details to admin email
        """
        try:
            subject = ADMIN_MAIL_SUBJECT.format(full_name=self.enquiry.full_name)

            html_content = ADMIN_EMAIL_CONTENT.format(enq=self.enquiry)
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=DEFAULT_FROM_EMAIL, to=[ADMIN_EMAIL],)
            email.attach_alternative(html_content, "text/html")
            email.send(fail_silently=False)

            return True

        except Exception as exc:
            print(FAIL_TO_SEND_ADMIN_NOTIFICATION.format(enquiry_id=self.enquiry.id))
            print(str(exc))
            return False

    def send_user_confirmation(self):
        """
        Send confirmation email to user
        """
        try:
            subject = USER_CONFIRMATION_SUBJECT

            html_content = USER_EMAIL_CONTENT.format(enq_full_name=self.enquiry.full_name)
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=DEFAULT_FROM_EMAIL, to=[self.enquiry.email])

            email.attach_alternative(html_content, "text/html")
            email.send(fail_silently=False)

            return True

        except Exception as exc:
            print(FAIL_TO_SEND_USER_NOTIFICATION.format(email=self.enquiry.email))
            print(str(exc))
            return False
        
class EnquiryService:

    @staticmethod
    def get_all_enquiries():
        return Enquiry.objects.all()
    
    @staticmethod
    def get_enquiry_by_id(pk):
        return get_object_or_404(Enquiry, pk=pk)

    @staticmethod
    def create_enquiry(validated_data):
        return Enquiry.objects.create(**validated_data)

    @staticmethod
    def update_enquiry(instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete_enquiry(instance):
        instance.delete()