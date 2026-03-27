from .models import Enquiry
from django.shortcuts import get_object_or_404

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