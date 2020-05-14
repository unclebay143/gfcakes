from django.shortcuts import render, get_object_or_404
from .models import Cake
from .forms import PostCake
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

def Link(request):
    return render(request, 'link.html')

def Index(request):
    return render(request, 'index.html')


def  Cakes(request):
    post_list = Cake.objects.all()
    paginator = Paginator(post_list, 8)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list= paginator.page(paginator.num_pages)
    return render(request, 'cakes.html',{'page': page, 'post_list': post_list})
def cakeinfo(request):
    model = Cake
    return render(request, 'cake_info.html')

def Contact(request):
    return render(request, 'contact.html')

def Store(request):

    return render(request, 'store.html')

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