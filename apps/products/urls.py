from django.conf.urls.static import static
from django.urls import path

from .views import CategoryAddProductView, CategoryListCreateView, ProductListCreateView, ReadUpdateDeleteView

from config import settings

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='productList'),
    path('/<int:pk>', ReadUpdateDeleteView.as_view(), name='product_read_update_delete'),

    path('/category', ProductListCreateView.as_view(), name='productList_by_category'),
    path('/category/getAll', CategoryListCreateView.as_view(), name='productList_by_category'),
    path('/category/create', CategoryListCreateView.as_view(), name='category_create'),
    path('/category/<int:pk>/add_product', CategoryAddProductView.as_view(), name='category_create_product'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
