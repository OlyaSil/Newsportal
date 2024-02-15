from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsList.as_view(), name='post-list'),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('article/create/', ArticleCreate.as_view(), name='article-create'),
    path('news/create/', NewsCreate.as_view(), name='news-create'),
    path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news-update'),
    path('article/<int:pk>/update/', ArticleUpdate.as_view(), name='article-update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news-delete'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article-delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]
