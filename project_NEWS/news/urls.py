from django.urls import path
from .views import (NewsList, ArticlesList, PostDetail, NewsCreate,
                    ArticlesCreate, NewsEdit, ArticlesEdit,
                    ArticlesDelete, NewsDelete, PostSearch, subscribe, NotificationList
                    )


urlpatterns = [
    path('news/', NewsList.as_view(), name='post_list'),
    path('articles/', ArticlesList.as_view(), name='post_list'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('search/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('articles/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticlesCreate.as_view(), name='news_create'),
    path('articles/<int:pk>/edit/', ArticlesEdit.as_view(), name='news_edit'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='news_delete'),
    path('subscribe/', subscribe, name='subscribe'),
    path('subscribe/notification', NotificationList.as_view(), name='notification')
]

