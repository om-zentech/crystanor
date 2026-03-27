import logging
from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from response_utils.custom_response import ApiResponse, get_error_message_list

logger = logging.getLogger('watchtower')

def custom_exception_handler(exc, context):
    from rest_framework.views import exception_handler

    # HANDLE 404 FIRST
    if isinstance(exc, Http404):
        error_message = "Resource not found"
        logging_exception(error_message, context.get('request'))
        return ApiResponse(
            status=0,
            message=error_message,
            data=None,
            http_status=status.HTTP_404_NOT_FOUND
        ).create_response()

    # Default DRF handler
    response = exception_handler(exc, context)

    # If DRF can't handle it → treat as server error
    if response is None:
        logging_exception(str(exc), context.get('request'))
        return ApiResponse(
            status=0,
            message="Internal server error",
            data=None,
            http_status=status.HTTP_500_INTERNAL_SERVER_ERROR
        ).create_response()

    # Validation errors
    if isinstance(exc, ValidationError):
        logging_exception(get_error_message_list(exc), context.get('request'))
        return ApiResponse(
            status=0,
            message=get_error_message_list(exc),
            data=None,
            http_status=status.HTTP_400_BAD_REQUEST
        ).create_response()

    # Other handled errors (fallback)
    logging_exception(str(exc), context.get('request'))
    return ApiResponse(
        status=0,
        message=str(exc),
        data=None,
        http_status=response.status_code
    ).create_response()


def logging_exception(exc, request):
    logger.debug(msg=exc, exc_info=True)