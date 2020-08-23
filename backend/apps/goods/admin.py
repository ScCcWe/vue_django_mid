from django.contrib import admin

from .models import GoodsCategory, GoodsCategoryBrand, Goods, IndexAd, GoodsImage, Banner, HotSearchWords

admin.site.register(GoodsCategory)
admin.site.register(GoodsCategoryBrand)
admin.site.register(Goods)
admin.site.register(IndexAd)
admin.site.register(GoodsImage)
admin.site.register(Banner)
admin.site.register(HotSearchWords)
