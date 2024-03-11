from django.shortcuts import render
from datetime import datetime
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView


class NewsList(ListView):
    model = Post
    ordering = '-date_time_creation_post'
    template_name = 'news.html'
    context_object_name = 'posts'
    # paginate_by = 10

    # Переопределяем функцию получения списка товаров
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = PostFilter(self.request.GET, queryset)
    #     return queryset.filter(post_or_news='NEWS')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['filterset'] = self.filterset
        # context['time_now'] = datetime.now()
        # context['next_sale'] = None
        return context


class ArticlesList(ListView):
    model = Post
    ordering = '-date_time_creation_post'
    template_name = 'articles.html'
    context_object_name = 'posts'
    # paginate_by = 10

    # # Переопределяем функцию получения списка товаров
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = PostFilter(self.request.GET, queryset)
    #     return queryset.filter(post_or_news='POST')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.filterset
    #     context['next_sale'] = None
    #     return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'