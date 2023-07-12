"""
URL configuration for catalog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

# http://127.0.0.1:8000/admin

urlpatterns = [
    path('',include('pages.urls')), # pages sayfası altındaki url dosyası çağırılacak
    path('admin/', admin.site.urls), # ilk başa admin/ yazıldığı için localhostta 8000'den sonra hep admin olacağı anlamına gelir
    path('user/', include('user.urls')), # user altında oluşturduğumus urls.py dosyasında yer alan register, logout gibi işlemler user/'tan sonra gelmesi için bu satır oluşturuldu
    path('movies/', include('movies.urls')),
]
