from .models import Category
from .serializers import CategorySerializer
from rest_framework.viewsets import ModelViewSet


class CategoriesViewSet(ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
