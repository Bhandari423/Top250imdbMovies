from django.contrib import admin
from movie.models import TopMovie

# Register your models here.
class TopMovieAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "rating", "director", "cast")
    list_filter = ('rating',)
    search_fields = ['title',]


admin.site.register(TopMovie, TopMovieAdmin)