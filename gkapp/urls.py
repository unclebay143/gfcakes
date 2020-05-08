from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Index, Cakes, Link, Contact, Store, Upload, Fond
urlpatterns = [
    path('', Index, name='index'),
    path('cakes', Cakes, name='cakes'),
    path('links', Link, name='links'),
    path('contact/', Contact, name='contact'),
    path('store', Store, name='store'),
    path('upload', Upload, name='upload'),
    path('fond', Fond, name='fond')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)