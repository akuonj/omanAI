# urls.py

from django.urls import path

from . import views


urlpatterns = [

    path('omanAI/', views.detect_objects, name='home'),

]

