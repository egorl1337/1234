from django import views
from django.urls import path
from .views import signup

urlpatterns = [
    path('reg/', signup.as_view(), name = 'reg')



]