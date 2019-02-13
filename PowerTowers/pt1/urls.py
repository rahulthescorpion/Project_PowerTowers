from django.conf.urls import url,include
from pt1 import views


app_name = 'pt1'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^invbat/',views.invbat,name='invbat'),
    url(r'^water/',views.water,name='water'),
    url(r'^solar/',views.solar,name='solar'),
    url(r'^contact/',views.contact,name='contact'),
]
