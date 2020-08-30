from rest_framework import generics, mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .filters import GoodsFilter
from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer


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

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # 自定义过滤器
    filter_class = GoodsFilter

    search_fields = ('name', 'goods_brief')

    ordering_fields = ('shop_price', 'add_time')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品分类
    """
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer
    pagination_class = GoodsPagination
