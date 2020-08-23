from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Goods
from .serializers import GoodsSerializer


class GoodsListView(APIView):
    """
    商品列表
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)
