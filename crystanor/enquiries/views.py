from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import EnquirySerializer
from .services import EnquiryService
from .models import Enquiry
from response_utils.custom_response import ApiResponse
from .constants import (SUCCESSFULLY_CREATED_ENQUIRY, SUCCESSFULLY_FETCHED_ENQUIRY,
                        SUCCESSFULLY_DELETED_ENQUIRY, SUCCESSFULLY_UPDATED_ENQUIRY, NO_DATA_FOUND)

class EnquiryAPIView(APIView):
    """
    API endpoint to manage Enquiry
    """
    def get(self, request):
        """
        Fetch all enquiries
        """
        enquiries = EnquiryService.get_all_enquiries()

        if not enquiries.exists():
            return ApiResponse(
                status=1,
                message=NO_DATA_FOUND,
                data=[],
                http_status=status.HTTP_200_OK
            ).create_response()

        serializer = EnquirySerializer(enquiries, many=True)

        return ApiResponse(
            status=1,
            message=SUCCESSFULLY_FETCHED_ENQUIRY,
            data=serializer.data,
            http_status=status.HTTP_200_OK
        ).create_response()

    def post(self, request):
        """
        Create a new enquiry
        """
        serializer = EnquirySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        enquiry = EnquiryService.create_enquiry(serializer.validated_data)

        return ApiResponse(
            status=1,
            message=SUCCESSFULLY_CREATED_ENQUIRY,
            data=EnquirySerializer(enquiry).data,
            http_status=status.HTTP_201_CREATED
        ).create_response()

class EnquiryDetailAPIView(APIView):
    """
    API endpoint to handle a single enquiry by ID   
    """
    def get_object(self, pk):
        """
        Get an enquiry object by primary key
        """
        return get_object_or_404(Enquiry, pk=pk)

    def get(self, request, pk):
        """
        Fetch a single enquiry by ID
        """
        enquiry = self.get_object(pk)

        return ApiResponse(
            status=1,
            message=SUCCESSFULLY_FETCHED_ENQUIRY,
            data=EnquirySerializer(enquiry).data,
            http_status=status.HTTP_200_OK
        ).create_response()

    def put(self, request, pk):
        """
        Update an existing enquiry
        """
        enquiry = self.get_object(pk)

        serializer = EnquirySerializer(enquiry, data=request.data)
        serializer.is_valid(raise_exception=True)

        updated_enquiry = EnquiryService.update_enquiry(enquiry, serializer.validated_data)

        return ApiResponse(
            status=1,
            message=SUCCESSFULLY_UPDATED_ENQUIRY,
            data=EnquirySerializer(updated_enquiry).data,
            http_status=status.HTTP_200_OK
        ).create_response()

    def delete(self, request, pk):
        """
        Delete an existing enquiry
        """
        enquiry = self.get_object(pk)

        EnquiryService.delete_enquiry(enquiry)

        return ApiResponse(
            status=1,
            message=SUCCESSFULLY_DELETED_ENQUIRY,
            data=None,
            http_status=status.HTTP_204_NO_CONTENT
        ).create_response()