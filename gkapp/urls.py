from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Index, Cakes, cakeinfo, Link, Contact, Store, Upload, prototype
urlpatterns = [
    path('', Index, name='index'),
    path('cakes', Cakes, name='cakes'),
    path('links', Link, name='links'),
    path('contact/', Contact, name='contact'),
    path('store', Store, name='store'),
    path('upload', Upload, name='upload'),
    path('prototype', prototype, name='prototype'),
    path('cakeinfo/<int:pk>/', cakeinfo, name='cakeinfo')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)