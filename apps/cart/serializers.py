from rest_framework.serializers import ModelSerializer

from .models import CartModel, CartItemModel
from ..products.serializers import ProductSerializer


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItemModel
        fields = (
            'id',
            # 'product',
            'quantity',
            'price_ht',
            # 'cart',
            # 'description',
            # 'stock',
            # 'created',
            # 'updated'
        )


class CartSerializer(ModelSerializer):
    product_id = ProductSerializer(many=True)

    class Meta:
        model = CartModel
        fields = ('id',
                  # 'user',
                  'created_at',
                  # 'products'
                  )

