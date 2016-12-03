from django.conf.urls import url
from voda import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^where$', views.where, name='where'),
    url(r'^about$', views.about, name='about'),
]
