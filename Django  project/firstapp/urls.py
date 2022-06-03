from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path("", views.index, name="firstapp"),
    path("about", views.about, name="about"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("contact", views.contacttest, name="contact"),
    #  path("usama", views.usama, name="usama")
    
    
   


]
