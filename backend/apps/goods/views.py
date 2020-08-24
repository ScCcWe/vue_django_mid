from rest_framework.response import Response
from rest_framework.views import APIView

# mixins和generic一起使用
# generics.GenericAPIView 继承APIView，封装了许多方法，比APIView功能更加强大
# 用的时候需要定义queryset和serializer_class
from rest_framework import mixins, generics

from .models import Goods
from .serializers import GoodsSerializer


# ListModelMixin里面list方法帮我们做好了分页和序列化的工作
class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
