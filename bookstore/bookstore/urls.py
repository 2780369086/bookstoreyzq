from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # 用户模块
    url(r'^user/', include('users.urls', namespace='user')),
    # 富文本编辑器
    url(r'^tinymce/', include('tinymce.urls')),
    # 商品模块
    url(r'^', include('books.urls', namespace='books')),
#     购物车模块
    url(r'^cart/', include('cart.urls', namespace='cart')),
# 订单模块
	url(r'^order/', include('order.urls', namespace='order')),
#     评论模块
    url(r'^comment/', include('comments.urls', namespace='comment')),

    url(r'^search/',include('haystack.urls')),

]
