from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.index_view, name='index'),
    path(
        #詳細ページのURLはblog-detail/レコードのid
        'blog-detail/<int:pk>/',
        #viewモジュールのblog detailを実行
        views.blog_detail,
        #URLパターンの名前をblog_detailにする
        name='blog_detail'
        ),
]
