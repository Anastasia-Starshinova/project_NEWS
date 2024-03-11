from django.urls import path
from .views import NewsList, ArticlesList, PostDetail

# from .views import (NewsList, PostDetail,
#                     CategoriesList, CommentsList, CommentDetail,
#                     NewsCreate, NewsEdit, NewsDelete, PostSearch, ArticlesList,
#                     ArticlesDelete, ArticlesCreate, ArticlesEdit)


urlpatterns = [
    path('news/', NewsList.as_view(), name='post_list'),
    path('articles/', ArticlesList.as_view(), name='post_list'),
    # path('search/', PostSearch.as_view(), name='post_search'),
    path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('articles/<int:pk>', PostDetail.as_view(), name='post_detail'),
    # path('categories/', CategoriesList.as_view()),
    # path('comments/', CommentsList.as_view()),
    # path('comments/<int:pk>', CommentDetail.as_view()),
    #
    # # еще вариант страницы с созданием поста
    # # path('news/create/', create_post, name='post_create'),
    #
    # path('news/create/', NewsCreate.as_view(), name='news_create'),
    # path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    # path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    # path('articles/create/', ArticlesCreate.as_view(), name='news_create'),
    # path('articles/<int:pk>/edit/', ArticlesEdit.as_view(), name='news_edit'),
    # path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='news_delete'),


]

# urlpatterns = [
#     path('news/', NewsList.as_view(), name='post_list'),
#     path('articles/', ArticlesList.as_view(), name='post_list'),
#     path('search/', PostSearch.as_view(), name='post_search'),
#     path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
#     path('articles/<int:pk>', PostDetail.as_view(), name='post_detail'),
#     path('categories/', CategoriesList.as_view()),
#     path('comments/', CommentsList.as_view()),
#     path('comments/<int:pk>', CommentDetail.as_view()),
#
#     # еще вариант страницы с созданием поста
#     # path('news/create/', create_post, name='post_create'),
#
#     path('news/create/', NewsCreate.as_view(), name='news_create'),
#     path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
#     path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
#     path('articles/create/', ArticlesCreate.as_view(), name='news_create'),
#     path('articles/<int:pk>/edit/', ArticlesEdit.as_view(), name='news_edit'),
#     path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='news_delete'),
#
#
# ]