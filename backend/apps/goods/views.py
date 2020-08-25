from rest_framework import generics, mixins, viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Goods
from .serializers import GoodsSerializer


class GoodsPagination(PageNumberPagination):
    """
    商品列表自定义分页
    """
    # 默认每页显示的数量
    page_size = 10
    # 可以动态改变每页显示的个数
    page_size_query_param = "page_size"
    # 页码参数 127.0.0.1:8000/goods/?page=2&page_size=30
    page_query_param = 'page'
    # 每页最多能显示多少体条（仅当page_size_query_param设置时有效）
    max_page_size = 20


# 使用generics.ListAPIView来进一步的简化代码
class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
