from django.urls import path
from .views import main
from . import views

urlpatterns = [
    path("home", views.main, name="main"),
    
]
