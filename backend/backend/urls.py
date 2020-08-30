"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
import debug_toolbar

from backend.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'goods', GoodsListViewSet, basename='goods')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('media/<path:path>', serve, {"document_root": MEDIA_ROOT}),
    # path('goods/', goods_list, name='goods'),
    path('', include(router.urls)),

    path('api-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title='生鲜超市')),

    path('debug-tool/', include(debug_toolbar.urls)),
]
