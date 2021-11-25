
from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('modul/', include('templateModul.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)