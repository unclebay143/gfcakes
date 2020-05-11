from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import PostCake
# Create your views here.

def Link(request):
    return render(request, 'link.html')

def Index(request):
    return render(request, 'index.html')


def  Cakes(request):
    post = Cake.objects
    return render(request, 'cakes.html', {"post":post})

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

def Fond(request):
    paginate_by = 3
    return render(request, 'fond.html')