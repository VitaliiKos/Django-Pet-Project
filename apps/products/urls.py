from django.urls import path
from .views import ProductListCreateView, ReadUpdateDeleteView,CategoryListCreateView,CategoryAddProductView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='productList_read_update_delete'),
    path('/<int:pk>', ReadUpdateDeleteView.as_view(), name='product_read_update_delete'),

    path('/category', ProductListCreateView.as_view(), name='productList_by_category'),
    path('/category/getAll', CategoryListCreateView.as_view(), name='productList_by_category'),
    path('/category/create', CategoryListCreateView.as_view(), name='category_create'),
    path('/category/<int:pk>/add_product', CategoryListCreateView.as_view(), name='category_create'),
]
