from django.urls import path
from .views import Index, Cakes, Link, Contact, Store
urlpatterns = [
    path('', Index, name='index'),
    path('cakes', Cakes, name='cakes'),
    path('links', Link, name='links'),
    path('contact/', Contact, name='contact'),
    path('store', Store, name='store')

]