from rest_framework import generics

from .models import Goods
from .serializers import GoodsSerializer


# 使用generics.ListAPIView来进一步的简化代码
class GoodsListView(generics.ListAPIView):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
