from django import forms
from .models import Article

class ArticleForm(forms.ModelForm): 
    # 모델에 어울리는 html 폼을 생성(input만 생성)

    class Meta(): # Meta 클래스 안에 사용할 모델 설정 
        model = Article
        fields = '__all__'  
