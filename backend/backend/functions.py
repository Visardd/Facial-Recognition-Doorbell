from django.contrib.auth import login, logout, authenticate
from rest_framework import permissions, status
from rest_framework.response import Response

def LoginUser(request, username, password):
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return True, username
    
    return False, None