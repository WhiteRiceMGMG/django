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

    path(
        #scienceカテゴリ一覧urlはscience-list
        'science-list/',
        #viewモジュールのscience-view関数を実行
        views.science_view,
        #urlパターンの名前をscience_listにする
        name='science_list'
        ),

    path(
        'dailylife-list/',
        views.dailylife_view,
        name='dialylife_list'
        ),

    path(
        'music-list/',
        views.music_view,
        name='music_list'
        ),
]
