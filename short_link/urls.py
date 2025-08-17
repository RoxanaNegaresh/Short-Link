"""
URL configuration for short_link project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from create_link import views as C_views
from redirect import views as R_views
from create_QRcode import views as Q_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',C_views.index,name='index'),
    path('create/',C_views.create_link,name='create'),
    path('<str:shortlink>',R_views.redirect_,name="re"),
    path('qr/',Q_views.create_QRcode,name="qr")
]
