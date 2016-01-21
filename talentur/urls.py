from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^fb_login/', views.fb_login, name = 'fb_login')
]