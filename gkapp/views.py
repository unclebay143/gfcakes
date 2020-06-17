from django.shortcuts import render, get_object_or_404
from .models import Cake
from .forms import PostCake
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
import os
from django.templatetags.static import static
# Create your views here.

def Link(request):
    return render(request, 'link.html')

def Index(request):
    return render(request, 'index.html')


def  Cakes(request):
    post_list = Cake.objects.all()
    paginator = Paginator(post_list, 12)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list= paginator.page(paginator.num_pages)
    return render(request, 'cakes.html',{'page': page, 'post_list': post_list})


def Contact(request):
    return render(request, 'contact.html')

def Store(request):
    info_list = Cake.objects.all()
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path)
    paginator = Paginator(img_list, 15)
    page = request.GET.get('page')
    try:
        img_list = paginator.page(page)
    except PageNotAnInteger:
        img_list = paginator.page(1)
    except EmptyPage:
        img_list= paginator.page(paginator.num_pages)
    return render(request, 'store.html',{'page': page, 'post_list': img_list, 'images':img_list, 'i':info_list})

def Upload(request):
    form = PostCake() 
    
    if request.method == 'POST':
        form = PostCake(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'upload.html', context)

def prototype(request):
    return render(request, 'prototype.html')

def boot(request):
    images = Cake.objects.all()
    context = {
        "img":images
    }
    return render(request, 'bootstrap-cake.html', context)