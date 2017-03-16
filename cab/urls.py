from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from cab_sharing import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', auth_views.login,name="login"),
    url(r'^cabsharing', views.display_drivers, name = 'display_drivers'),    
    url(r'^update', views.update_status, name = 'update_status'),
    url(r'^login', views.login, name = 'login'),
    url(r'^register', views.register,name = 'register')
]