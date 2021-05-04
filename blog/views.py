from django.shortcuts import render
from .models import Blog
from .models import Personalblog
# Create your views here.

def blog(request):
    blog = Blog.objects.all()
    context = {
        "blog":blog
    }
    return render(request, 'album/index.html', context)


def personalblog(request):
    personalblog = Personalblog.objects.all()
    context = {
        "personalblog":personalblog
    }
    return render(request, 'blueberry/index.html', context)