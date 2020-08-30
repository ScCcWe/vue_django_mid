# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: serializers.py
# author: ScCcWe
# time: 2020/8/24 0:51

from rest_framework import serializers

from .models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    """
    三级分类
    """
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    """
    二级分类
    """
    # 在parent_category字段定义的related_name="sub_cat"
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    商品一级类别序列化
    """
    # 在parent_category字段定义的related_name="sub_cat"
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


# ModelSerializer实现商品列表页
class GoodsSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'
