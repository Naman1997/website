from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from mysite.core import views as core_views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^home/', core_views.home, name='home'),
    url(r'^login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/', core_views.signup, name='signup'),
    url(r'^/mysite/general', core_views.general),
]