from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^general/$', views.general, name='general'),
    url(r'^$', views.post_list, name='base'),
    url(r'^$', views.post_list, name='home'),
    url(r'^$', views.post_list, name='login'),
    url(r'^$', views.post_list, name='signup'),
]