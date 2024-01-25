from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reuniao.urls')),
    path('', include('django_dyn_dt.urls')), 
]