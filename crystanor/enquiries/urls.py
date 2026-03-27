from django.urls import path
from .views import EnquiryAPIView, EnquiryDetailAPIView

urlpatterns = [
    path('enquiries', EnquiryAPIView.as_view()),
    path('enquiries/<int:pk>', EnquiryDetailAPIView.as_view()),
]