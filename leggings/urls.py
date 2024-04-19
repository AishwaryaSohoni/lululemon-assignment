from django.urls import path

from . import views

urlpatterns = [
    path("", views.WomensLeggingsInfoView.as_view(), name="womens-leggings"),
]