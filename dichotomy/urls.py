from django.conf.urls import url

from . import views

app_name = 'dichotomy'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^api/create_workplace$', views.create_workplace, name='create_workplace'),
    url(r'^api/create_workplace/(?P<id>[0-9]+)/$', views.get_workplace, name='get_workplace'),
    url(r'^api/create_workplace/(?P<get_all>[0-9]+)/$', views.get_workplaces, name='get_workplaces'),
    url(r'^api/calculate_dichotomy$', views.calculate_dichotomy, name='calculate_dichotomy'),





]
