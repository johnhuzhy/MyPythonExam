from django.contrib import admin
from .models import ArticleColumn

class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ('user', 'column', 'created')
    list_filte = ('column',)


admin.site.register(ArticleColumn, ArticleColumnAdmin)