from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#recuperacion passw
from django.urls import path 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('empleados/',views.empleados_lista_api,name='empleados_lista_api'),


]