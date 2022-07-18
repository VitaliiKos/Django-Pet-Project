from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products', include('apps.products.urls')),
    path('cart', include('apps.cart.urls')),
    path('users', include('apps.user.urls')),
    path('auth', include('apps.auth.urls')),
]
