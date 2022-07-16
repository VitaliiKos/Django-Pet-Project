from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.cart.serializers import CartSerializer, CartItemSerializer
from .models import CartModel, CartItemModel


# -------------- Cart Views --------------------------------------
class ReadUpdateDeleteViewCart(ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = CartModel.objects.all()


# -------------- CartItem Views --------------------------------------
class ReadUpdateDeleteViewCartItem(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItemModel.objects.all()


class CartItemListCreateView(ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItemModel.objects.all()

# ///////////////////////////////////////////////////////////////////////

# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.http import require_POST
# from requests import Response
# from rest_framework import status
#
# from apps.products.models import ProductModel
# from .cart import Cart
# from .forms import CartAddProductForm
#
#
# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(ProductModel, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#     # return redirect('cart:cart_detail')
#     return Response(status.HTTP_201_CREATED)
#
#
# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(ProductModel, id=product_id)
#     cart.remove(product)
#     # return redirect('cart:cart_detail')
#     return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# def cart_detail(request):
#     cart = Cart(request)
#     return cart
