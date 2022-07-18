from rest_framework.serializers import ModelSerializer

from .models import CategoryModel, ProductModel


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'category', 'price', 'image',  'description', 'stock', 'created', 'updated')


class CategorySerializer(ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = CategoryModel
        fields = ('id',
                  'name',
                  # 'slug',
                  'products')

