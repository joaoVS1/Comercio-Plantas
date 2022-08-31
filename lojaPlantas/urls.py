from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plantas/', include('plantas.urls')),
    path('', include('home.urls')),
    path('users/',include('users.urls')),
    path('comprar/', include('compras.urls'))
]
