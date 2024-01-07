from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Exists, OuterRef
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *
from .forms import NewsForm, ArticlesForm
from .filters import PostFilter

from django.http import HttpResponse


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
    paginate_by = 10 #количество записей на странице

    def get_queryset(self):#представление для фильтрации списка новостей и статей от filter.py
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации. self.request.GET содержит объект QueryDict
        # Сохраняем нашу фильтрацию в объекте класса,чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        all_news = Post.objects.all().values_list('post_name')
        context['count_news'] = all_news
        context['news_count'] = f"Всего новостей - {len(all_news)}"
        context['filterset'] = self.filterset  # Добавляем в контекст объект фильтрации.
        return context


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


# Добавляем новое представление для создания статей. Для отображения формы из шаблона и forms.py.
class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.news_create',)
    raise_exception = True
    # Указываем нашу разработанную форму, модель товаров и новый шаблон, в котором используется форма.
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'NE'
        return super().form_valid(form)


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.articles_create',)
    raise_exception = True
    form_class = ArticlesForm
    model = Post
    template_name = 'articles_edit.html'
    # success_url = reverse_lazy('post_detail')
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'AR'
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.news_update',)
    raise_exception = True
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'NE'
        return super().form_valid(form)


class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.articles_update',)
    raise_exception = True
    form_class = ArticlesForm
    model = Post
    template_name = 'articles_edit.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'AR'
        return super().form_valid(form)


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.news_delete',)
    raise_exception = True
    # form_class = NewsForm
    model = Post
    template_name = 'news_delete.html'
    success_url = "/news/" #reverse_lazy('news_list')

    # def get_success_url(self):
    #     return reverse_lazy('news_list') #, kwargs={'pk': self.object.pk})


class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.articles_delete',)
    raise_exception = True
    model = Post
    template_name = 'articles_delete.html'
    success_url = "/news/"


class CategoryList(LoginRequiredMixin, ListView):
    model = Post
    ordering = 'time_of_creation'
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'
    paginate_by = 10

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])         #профилактика ошибки 500
        queryset = Post.objects.filter(post_category=self.category).order_by('time_of_creation')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required()
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку публикаций категории '

    return render(request, 'subscribe.html', {'category': category, 'message': message})


@login_required()
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)

    message = 'Вы успешно отписались от рассылки публикаций категории '

    return render(request, 'subscribe.html', {'category': category, 'message': message})
