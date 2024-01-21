from django import forms
from .models import Post
class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'author',
           'title',
           'text',
           'categories',
       ]
       labels = {
           'author': 'Автор',
           'type': 'Тип',
           'title': 'Заголовок',
           'text': 'Текст',
           'categories': 'Категории',
       }

class NewsForm(PostForm):
    pass

class ArticleForm(PostForm):
    pass