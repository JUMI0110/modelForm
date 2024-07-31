from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def create(request):
    # new : 빈종이를 보여주는 기능 
    # create : 사용자가 입력한 데이터를 저장
    # --------- 메소드 차이에 의해 보여지는 기능 
    # GET create/ 빈종이를 보여주는 기능
    # POST create/ 사용자가 입력한 데이터를 저장

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        if form.is_valid(): # 들어온 데이터 유효한지 검증
            form.save()
            return redirect('articles:index')
            
        # else: 
            # 제대로 넣은 데이터는 남을 수 있게 새로운 form에 다시 request.POST 넣고 다시 보내주는 기능
            # form = ArticleForm(request.POST) 위에 선언된 form 사용

            # context = {
            #     'form': form
            # }
            # return render(request, 'create.html', context)
            
    else: 
        form = ArticleForm()

    context = {
        'form': form
    }
    return render(request, 'create.html', context)