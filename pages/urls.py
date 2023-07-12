from django.urls import path
from . import views

# http://127.0.0.1:8000

urlpatterns=[
    path('', views.index, name='index'), # views sayfasındaki index metodunu çağırdık ve bunun için localhosttan erişebilmek için url oluşturmuş olduk
    path('about/', views.about, name='about')
] # 8000'den sonra bir şey yazmıyorsa index sayfası gelecek. Eğer about yazıyorsa about sayfası gelecek