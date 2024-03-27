from django.shortcuts import render
from datetime import datetime
from .models import Post, User
from .filters import PostFilter
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.core.mail import send_mail


class NewsList(ListView, PermissionRequiredMixin):
    permission_required = ('news.view_post', )
    model = Post
    ordering = '-date_time_creation_post'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return queryset.filter(post_or_news='NEWS')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


# class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post', 'news.view_post',
                          )
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_or_news = 'NEWS'
        return super().form_valid(form)


# class NewsEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
class NewsEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post', 'news.view_post',
                           )
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post', 'news.view_post',
                           )
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')


class ArticlesList(ListView, PermissionRequiredMixin):
    permission_required = ('news.view_post',)
    model = Post
    ordering = '-date_time_creation_post'
    template_name = 'articles.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return queryset.filter(post_or_news='POST')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


# class ArticlesCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
class ArticlesCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post', 'news.view_post',
                           )
    form_class = PostForm
    model = Post
    template_name = 'articles_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_or_news = 'POST'
        return super().form_valid(form)


class ArticlesEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post', 'news.view_post',
                           )
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'


class ArticlesDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post', 'news.view_post',
                           )
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('post_list')


class PostSearch(ListView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        # context['time_now'] = datetime.now()
        context['filterset'] = self.filterset
        context['next_sale'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


@login_required
def subscribe(request):
    user = request.user

    # post = найти актуальный пост
    # actual_category = получить категорию поста
    # user.subscriptions.add(actual_category) добавить категорию и юзера в базу данных
    send_mail(
        subject='Вы подписались на категорию: ',
        # имя клиента и дата записи будут в теме для удобства
        message='Вы подписались на категорию: ',  # сообщение с кратким описанием проблемы
        from_email='starschinowa.anastasia@yandex.ru',  # здесь указываете почту, с которой будете отправлять (об этом попозже)
        recipient_list=[user.email, ]  # здесь список получателей. Например, секретарь, сам врач и т. д.
    )

    return redirect('/main/subscribe/notification')


class NotificationList(ListView):
    form_class = PostForm
    model = Post
    template_name = 'subscription_notification.html'
    # context_object_name = 'posts'