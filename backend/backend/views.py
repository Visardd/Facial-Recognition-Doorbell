from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from datetime import datetime
import datetime as dt
import calendar


class UserSignup(APIView):
    # permission_classes = () # Allows anyone to make a POST request
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        email = request.data["email"]
        username = request.data["username"]
        password = request.data["password"]
        
        user = User.objects.create_user(username=username, email=email, password=password)
        print(user)
        return Response({}, status=status.HTTP_200_OK)

class UserLogin(APIView):
    # permission_classes = () # Allows anyone to make a POST request
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return Response({}, status=status.HTTP_200_OK)
        else:
            # No backend authenticated the credentials
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    

class UserLogout(APIView):
    # permission_classes = (permissions.IsAuthenticated,) # Must be logged in to make a request
    # authentication_classes = (SessionAuthentication,)
    
    def post(self, request):
        print(request.user)
        logout(request)
        print("Logged out")
        return Response(status=status.HTTP_200_OK)
