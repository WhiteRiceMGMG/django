from django.shortcuts import render

#paginatorをインポート
from django.core.paginator import Paginator

#モデルからBlogPostをインポート
from .models import BlogPost


def index_view(request):
    #トップページのビュー
    #テンプレートをレンダリングして戻り値として返す
    #Parameters:
    #    request(HTTPRequest):
    #        クライアントからのリクエスト情報を格納した
    #        HTTPRequestオブジェクト
    #Return(HTTPRequest):
    #    render()でテンプレートをレンダリングした結果
    #モデルBloPostのオ
    #ブジェクトにorder_by()を適用して，
    #BlogPostのレコードを投稿日時の降順で並び替える

    records = BlogPost.objects.order_by('-posted_at')

    paginator = Paginator(records,4)
    #getリクエストのURLにpageパラメータがある場合はその値を取得する．
    #pageパラメータがない場合はデフォルトで1を返すようにする．

    page_number = request.GET.get('page',1)
    #page()メソッドの引数にページ番号を取得し，
    #該当ページのレコードを取得する．

    pages = paginator.page(page_number)

    #render():
    #第一引数:HTTPRequestオブジェクト
    #第二引数:レンダリングするテンプレート
    #第三引数:テンプレートに引き渡すdict型のデータ
    #         {任意のキー:クエリの結果(レコードのリスト)}

    return render(request, 'index.html', {'orderby_records': pages})

def blog_detail(request, pk):
    '''
    pk:投稿記事のid
    '''
    record = BlogPost.objects.get(id=pk)
    return render(
        request, 'post.html', {'object': record})

def science_view(request):
    records = BlogPost.objects.filter(category='science').order_by('-posted_at')
    paginator = Paginator(records, 2)
    page_number = request.GET.get('page', 1)
    pages = paginator.page(page_number)
    return render(request, 'science_list.html', {'orderby_records': pages})

def dailylife_view(request):
    records = BlogPost.objects.filter(category='dailylife').order_by('-posted_at')
    paginator = Paginator(records, 2)
    page_number = request.GET.get('page',1)
    pages = paginator.page(page_number)
    return render(request, 'dailylife_list.html', {'orderby_records':pages})

def music_view(request):
    records = BlogPost.objects.filter(category='music').order_by('-posted_at')
    paginator = Paginator(records, 2)
    page_number = request.GET.get('page', 1)
    pages = paginator.page(page_number)
    return render(request, 'dailylife_list.html', {'orderby_records':pages})


