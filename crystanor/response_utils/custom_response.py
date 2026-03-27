from builtins import dict

from django.http import JsonResponse
from rest_framework.response import Response

"""
    This module contains class to prepare a proper server response and return it.
"""


class ApiResponse:
    """
        This is a class for constructing a common server response.

        Attributes:
            status (int): Status of api 0 or 1.
            message (int): message to be sent with response.
            data (dict): Data to be sent in api if not specified returns empty dict.
            http_status (HTTP_STATUS): This the http status sent with api if not specified explicitly rest framework will
                                        handle it.
        """

    def __init__(self, status: int, message: str = None, data: dict = None, http_status=None,
                 data_as_list=False):
        """
        :parameters
        -----------
        status:  Status to be sent in response.
        message: message to be sent with response.
        data:    Data to be sent in api, if not specified returns empty dict
        http_status: HTTP_STATUS of api, if not specified explicitly then handled by rest framework
        """
        self.response = dict()

        self.message = message
        self.status = status
        self.http_status = http_status

        if data:
            self.data = data
        elif data_as_list:
            self.data = list()
        else:
            self.data = dict()

    def create_response(self):
        """
        Creates a Response class object and returns it.

        :py:class:: `rest_framework.response.Response`
        :return: Returns the Response of rest_framework api.
        """
        self.response['status'] = self.status
        self.response['message'] = self.message
        self.response['data'] = self.data

        if self.http_status:
            return Response(self.response, status=self.http_status)
        else:
            return Response(self.response)

    def create_json_response(self):
        """
        Creates a Response class object and returns it.

        :py:class:: `rest_framework.response.Response`
        :return: Returns the Response of rest_framework api.
        """
        self.response['status'] = self.status
        self.response['message'] = self.message
        self.response['data'] = self.data

        if self.http_status:
            return JsonResponse(self.response, status=self.http_status)
        else:
            return JsonResponse(self.response)


def get_error_message(serializer):
    errors = list(serializer.errors.values())
    print(errors)
    error_keys = list(serializer.errors.keys())
    print(error_keys)
    error_message = errors[0][0]
    print(error_message)
    return error_message


def get_error_message_list(error):
    if type(error.detail) == list:
        error_message = error.detail[0]
    else:
        error_message = []
        for key, value in error.detail.items():
            error_message.append(f"{key}: {value[0]}")
        # print(list(error.detail.keys())[0])
        # error_message = list(error.detail.values())[0][0]
    return error_message


def get_error_message_list_str(error):
    if type(error.detail) == list:
        error_message = error.detail[0]
    else:
        error_message = {}
        for key, value in error.detail.items():
            error_message[f"{key}"] = str(value[0])
        # print(list(error.detail.keys())[0])
        # error_message = list(error.detail.values())[0][0]
    return str(error_message)