from django.conf.urls import url

from . import views

app_name = 'santa_app'

urlpatterns = [
    url(r'^$', views.register, name='index'),
]
