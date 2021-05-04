from django.urls import path, include

from . import views

app_name = "blog"

urlpatterns =[
    path('', views.blog, name = 'blog'),
    path('blog/', views.personalblog, name = 'personalblog')
]