from django.shortcuts import render, get_object_or_404
from .models import Cake, PostImage

# Create your views here.

def Link(request):
    return render(request, 'link.html')

def Index(request):
    return render(request, 'index.html')


def  Cakes(request):
    post = Cake.objects.all()
    return render(request, 'cakes.html', {"post":post})

def Contact(request):
    return render(request, 'contact.html')

def Store(request):
    return render(request, 'store.html')

def Upload(request):
    post = get_object_or_404(Cake)
    return render(request, 'upload.html',{
        'post':post,        
    })