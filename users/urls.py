from django.contrib import admin
from django.urls import path,include,re_path as url
from django.contrib.auth.views import LoginView,LogoutView

from . import views
urlpatterns = [
 url(r'^login/$', LoginView.as_view(template_name="../templates/users/login.html"),
 name='login'),
 url(r'^logout/$', views.logout_view, name='logout'),
 url(r'^register/$', views.register, name='register'),
]