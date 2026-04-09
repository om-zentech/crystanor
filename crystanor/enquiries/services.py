from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from crystanor.settings import DEFAULT_FROM_EMAIL, ADMIN_EMAIL
from enquiries.models import Enquiry
from enquiries.constants import USER_EMAIL_CONTENT, ADMIN_EMAIL_CONTENT, THANKS_FOR_ENQUIRY
from django.core.mail import EmailMultiAlternatives

class EmailService:

    def __init__(self, enquiry: Enquiry):
        self.enquiry = enquiry

    def send_admin_notification(self):
        subject = f"New Enquiry from {self.enquiry.full_name}"

        message = ADMIN_EMAIL_CONTENT.format(enq=self.enquiry)

        send_mail(subject, message, DEFAULT_FROM_EMAIL, [ADMIN_EMAIL], fail_silently=False,)

    def send_user_confirmation(self):
        subject = "We received your enquiry"

        html_content = USER_EMAIL_CONTENT.format(enq_full_name=self.enquiry.full_name)
        
        email = EmailMultiAlternatives(subject, THANKS_FOR_ENQUIRY, DEFAULT_FROM_EMAIL, [self.enquiry.email],)
        email.attach_alternative(html_content, "text/html")
        email.send()

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