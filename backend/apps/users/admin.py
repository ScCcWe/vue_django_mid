from django.contrib import admin

from .models import UserProfile, VerifyCode

# 在admin里面注册
# 注册UserProfile到admin中
admin.site.register(UserProfile)
admin.site.register(VerifyCode)
