from django.conf.urls import url
from restapi.cakeshop import views

urlpatterns = [
    url(r'^api/cakes$', views.cakes_list),
    url(r'^api/cakes/(?P<pk>[0-9]+)$', views.cake_detail),
]
