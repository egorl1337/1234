
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('e.urls')),
    path('shop', include('shop.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('register.urls'))
]


