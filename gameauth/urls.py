from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup),
    path("login/", views.login),
    path("renew-token/", views.renewToken),
]
