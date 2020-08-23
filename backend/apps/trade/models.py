from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from goods.models import Goods

User = get_user_model()


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=models.CASCADE)
    nums = models.IntegerField(default=0, verbose_name="购买数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name  # verbose_name的复数显示

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.nums)
