# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: views_base.py
# author: ScCcWe
# time: 2020/8/23 23:36
from django.forms import model_to_dict
from django.views.generic.base import View

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()
        for good in goods:
            json_dict = model_to_dict(good)
            json_list.append(json_dict)

        from django.http import HttpResponse
        import json
        # 返回json，一定要指定类型content_type='application/json'
        return HttpResponse(json.dumps(json_list, indent=4), content_type="application/json")
