from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from apps.products.models import CategoryModel, ProductModel
from apps.products.serializers import ProductSerializer, CategorySerializer


class ProductListCreateView(ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        # products = Product.objects.filter(available=True)
        products = ProductModel.objects.all()
        category_id = self.request.query_params.get('category_id', None)
        if category_id:
            products = products.filter(category__id__exact=category_id)
        return products


class ReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


# ------------------------------------------------

class CategoryListCreateView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()


class CategoryAddProductView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = CategoryModel.objects.all()

    def perform_create(self, serializer):
        # self.kwargs.get('pk')
        category = self.get_object()
        serializer.save(category=category)
