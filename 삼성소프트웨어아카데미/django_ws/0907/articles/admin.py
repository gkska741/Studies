from django.contrib import admin
from .models import Article
# Register your models here.
# Adminsite에 나의 클래스를 등록


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'updated_at')
    list_display_links = ('title',)
admin.site.register(Article)