from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
#    path('^admin/', include(admin.site.urls)),
#    path('^chaining/', include('smart_selects.urls')),
]