from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = [
        "discription",
        "thumbnail",
        "timecase"
        
    ]

admin.site.register(Blog,BlogAdmin)