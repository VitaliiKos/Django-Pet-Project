from django.conf.urls.static import static
from django.urls import include, path

from rest_framework import routers

from . import views

from config import settings

router = routers.DefaultRouter()
router.register(r'/cart', views.CartViewSet)
# router.register(r'delivery-cost', views.DeliveryCostViewSet)
# router.register(r'/user', views.UserViewSet)

urlpatterns = [
    path('', include((router.urls, 'apps.cart'))),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
