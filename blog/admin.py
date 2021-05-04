from django.contrib import admin
from .models import Blog 
from .models import Personalblog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = [
        "discription",
        "thumbnail",
        "timecase"
        
    ]

class PersonalblogAdmin(admin.ModelAdmin):
    list_display = [
        "blogtitle",
        "description",
        "thumbnail"

    ]

admin.site.register(Blog,BlogAdmin)
admin.site.register(Personalblog,PersonalblogAdmin)