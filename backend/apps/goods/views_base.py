# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: views_base.py
# author: ScCcWe
# time: 2020/8/23 23:36
from django.views.generic.base import View

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        goods = Goods.objects.all()

        from django.http import JsonResponse
        from django.core import serializers
        import json
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)
