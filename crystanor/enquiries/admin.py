from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):

    list_display = ("id", "full_name", "email", "company_name", "country",)

    search_fields = ("full_name", "email", "company_name",)

    list_filter = ("country",)