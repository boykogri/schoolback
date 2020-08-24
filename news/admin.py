# Register your models here.
from django.contrib import admin

from .models import NewsItem, NewsImage


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageInline, ]


admin.site.register(NewsImage)
admin.site.register(NewsItem, NewsAdmin)
