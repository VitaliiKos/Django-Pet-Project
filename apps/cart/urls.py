from django.urls import path
from config import settings
from django.conf.urls.static import static

from . import views
from .views import ReadUpdateDeleteViewCart,CartItemListCreateView

# Cart Urls

urlpatterns = [
    path('', ReadUpdateDeleteViewCart.as_view(), name='list-carts'),
    path('/<int:pk>', ReadUpdateDeleteViewCart.as_view(), name='detail-cart'),
    path('/create', ReadUpdateDeleteViewCart.as_view(), name='create-cart'),
    path('/<int:pk>/update', ReadUpdateDeleteViewCart.as_view(), name='update-cart'),
    path('/<int:pk>/delete', ReadUpdateDeleteViewCart.as_view(), name='delete-cart'),


    # CartItem Urls
    path('/cartitem', views.CartItemListCreateView.as_view(), name='list-cartItem'),
    path('/cartitem/<int:pk>', views.ReadUpdateDeleteViewCartItem.as_view(), name='detail-cartItem'),
    path('/cartitem/create', views.ReadUpdateDeleteViewCartItem.as_view(), name='create-cartItem'),
    path('/cartitem/<int:pk>/update', views.ReadUpdateDeleteViewCartItem.as_view(), name='update-cartItem'),
    path('/cartitem/<int:pk>/delete', views.ReadUpdateDeleteViewCartItem.as_view(), name='delete-cartItem'),

]

# CartItem Urls
# urlpatterns = [
#     path('cart/cartitem', views.ReadUpdateDeleteViewCartItem.as_view(), name='list-cartitem'),
#     path('cartitem/<int:pk>/', views.ReadUpdateDeleteViewCartItem.as_view(), name='detail-cartitem'),
#     path('cartitem/create/', views.ReadUpdateDeleteViewCartItem.as_view(), name='create-cartitem'),
#     path('cartitem/<int:pk>/update/', views.ReadUpdateDeleteViewCartItem.as_view(), name='update-cartitem'),
#     path('cartitem/<int:pk>/delete/', views.ReadUpdateDeleteViewCartItem.as_view(), name='delete-cartitem'),
# ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.urls import path
#
# from . import views
#
#
# urlpatterns = [
#     path('', views.cart_detail, name='cart_detail'),
#     path(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
#     path(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
# ]