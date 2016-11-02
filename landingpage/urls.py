from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landingpage, name='landingpage'),
    url(r'^register/$', views.register, name='register'),
]
