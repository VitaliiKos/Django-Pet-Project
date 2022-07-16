from django.conf.urls.static import static
from django.urls import path, include

from config import settings
from .views import ProductListCreateView, ReadUpdateDeleteView,CategoryListCreateView,CategoryAddProductView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='productList_read_update_delete'),
    path('/<int:pk>', ReadUpdateDeleteView.as_view(), name='product_read_update_delete'),

    path('/category', ProductListCreateView.as_view(), name='productList_by_category'),
    path('/category/getAll', CategoryListCreateView.as_view(), name='productList_by_category'),
    path('/category/create', CategoryListCreateView.as_view(), name='category_create'),
    path('/category/<int:pk>/add_product', CategoryAddProductView.as_view(), name='category_create_product'),

    # path('/cart', include('apps.cart.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)