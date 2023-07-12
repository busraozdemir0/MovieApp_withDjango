from django.contrib import admin
from .models import Movie # aynı dizin içerisinde olduğumuz için models başına nokta koyduk


class MovieAdmin(admin.ModelAdmin):
    list_display=('id','name','created_date','isPublished')
    list_display_links=('id','name')
    list_filter=('created_date',)
    list_editable=('isPublished',)
    list_per_page= 10 # her sayfada 10 kayıt olması için


# Register your models here.
admin.site.register(Movie, MovieAdmin)
