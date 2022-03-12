from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create_todo, name="form"),
    path("sign_up", views.sign_up, name="sign_up"),
]
