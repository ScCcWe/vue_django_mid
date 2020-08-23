from django.contrib import admin

from .models import UserFav, UserLeavingMessage, UserAddress

# 在admin里面注册
# 注册UserProfile到admin中
admin.site.register(UserFav)
admin.site.register(UserLeavingMessage)
admin.site.register(UserAddress)
