from rest_framework.views import APIView

from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from datetime import datetime
import datetime as dt
import calendar


class UserLogin(APIView): # User Login
    # permission_classes = () # Allows anyone to make a POST request
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        return Response({}, status=status.HTTP_200_OK)
