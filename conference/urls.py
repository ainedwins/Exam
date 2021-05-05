from django.urls import path

from . import views

app_name = "conference"

urlpatterns = [
    path('',views.home, name='home'),
]