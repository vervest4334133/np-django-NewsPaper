from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import *


class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'time_of_creation'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        all_news = Post.objects.all().values_list('post_name')
        context['count_news'] = all_news
        context['news_count'] = f"Всего новостей - {len(all_news)}"
        return context


# class CommentList(ListView):
#     model = Comment
#     ordering = 'comment_date'
#     template_name = 'news.html'
#     context_object_name = 'news'


class PostDetails(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'single_news.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'single_news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()

        return context
