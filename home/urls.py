from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('', views.HomePageView.as_view(), name='home'),
    url(r'^about/', views.AboutPageView.as_view(), name='about'),
]
