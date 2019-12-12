from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.loging, name='login'),
    path("register/", views.register, name='register'),
    path("status/", views.status, name='status'),
    path("logout/", views.logouting),
    path("", views.index, name='index')
]
