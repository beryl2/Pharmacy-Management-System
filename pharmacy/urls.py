from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from main_app import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginPage),
    
]
