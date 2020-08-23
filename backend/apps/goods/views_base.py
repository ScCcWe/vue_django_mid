# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: views_base.py
# author: ScCcWe
# time: 2020/8/23 23:36

from django.views.generic.base import View

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()
        for good in goods:
            json_dict = {}
            json_dict['name'] = good.name
            # json_dict['category'] = good.category
            json_dict['market_price'] = good.market_price
            json_list.append(json_dict)

        from django.http import HttpResponse
        import json
        return HttpResponse(json.dumps(json_list, indent=4), content_type="application/json")
