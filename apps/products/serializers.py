from rest_framework.serializers import ModelSerializer

from .models import ProductModel, CategoryModel


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'price', 'image', 'description', 'stock', 'created', 'updated')


class CategorySerializer(ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = CategoryModel
        fields = ('id', 'name', 'products')

