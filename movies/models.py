from django.db import models

# Create your models here.

# veritabanına yansıyacak olan Movie tablosu
class Movie(models.Model):
    name=models.CharField(max_length=100, verbose_name='Film Adı') # char
    description=models.TextField(verbose_name='Film Açıklaması') # textarea
    image = models.CharField(max_length=500, verbose_name='Film Resmi') # verbose_name='Film Resmi' => fiml eklerken image: yazması yerine Film Resmi: yazması için
    created_date=models.DateTimeField(auto_now_add=True, verbose_name='Film Eklenme Tarihi')
    isPublished=models.BooleanField(default=True) # filmin yayında olup olmadığı bilgisi (varsayılan True atadık)
    search_fields=('name','description') # arama inputu gelir


    def __str__(self):
        return self.name  # film ekledikten sonra filmin adı görünmesi için
    
    def get_image_path(self):
        return '/img/'+self.image
