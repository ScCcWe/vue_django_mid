# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: filters.py
# author: ScCcWe
# time: 2020/8/26 0:49

import django_filters
from django.db.models import Q

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品过滤的类
    """
    price_min = django_filters.NumberFilter(field_name="shop_price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(field_name="shop_price", lookup_expr="lte")
    top_category = django_filters.NumberFilter(method='top_category_filter', label='分类ID')

    # 自定义过滤方法，不管当前点击的是一级分类还是二级分类还是三级分类，都能找到
    def top_category_filter(self, queryset, name, value):
        return queryset.filter(
            Q(category_id=value)
            | Q(category_parent_category_id=value)
            | Q(category_parent_category_parent_category_id=value)
        )

    class Meta:
        model = Goods
        fields = ["price_min", "price_max"]
        ordering_fields = ('sold_num', 'shop_price')