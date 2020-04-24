from django.shortcuts import render

# Create your views here.

def Link(request):
    return render(request, 'link.html')

def Index(request):
    return render(request, 'index.html')


def  Cakes(request):
    return render(request, 'cakes.html')

def Contact(request):
    return render(request, 'contact.html')

def Store(request):
    return render(request, 'store.html')