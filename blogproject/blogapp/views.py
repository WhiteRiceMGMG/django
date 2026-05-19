from django.shortcuts import render

#モデルからBlogPostをインポート
from .models import BlogPost


def index_view(request):
    '''
    トップページのビュー
    テンプレートをレンダリングして戻り値として返す
    Parameters:
        request(HTTPRequest):
            クライアントからのリクエスト情報を格納した
            HTTPRequestオブジェクト
    Return(HTTPRequest):
        render()でテンプレートをレンダリングした結果
    モデルBloPostのオ
    ブジェクトにorder_by()を適用して，
    BlogPostのレコードを投稿日時の降順で並び替える
    '''

    records = BlogPost.objects.order_by('-posted_at')
    '''
    render():
    第一引数:HTTPRequestオブジェクト
    第二引数:レンダリングするテンプレート
  　第三引数:テンプレートに引き渡すdict型のデータ
             {任意のキー:クエリの結果(レコードのリスト)}
    '''

    return render(request, 'index.html', {'orderby_records': records})

def blog_detail(request, pk):
    '''
    pk:投稿記事のid
    '''
    record = BlogPost.objects.get(id=pk)
    return render(
        request, 'post.html', {'object': record})
