
from django.contrib import admin
from django.urls import path
from backend.views import *
from document.views import ImageView


urlpatterns = [
    path('upload/', ImageView.as_view(), name ='image-upload'),
    path('admin/', admin.site.urls),
    path('signup/', UserSignup.as_view()),
    path('login/', UserLogin.as_view()),
    path('logout/', UserLogout.as_view()),
    
]
