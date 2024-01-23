from django.urls import path
from .views import (PostList, PostDetails, NewsCreate, ArticlesCreate, NewsUpdate, ArticlesUpdate, NewsDelete,
                    ArticlesDelete, CategoryList, subscribe, unsubscribe, SubscriptionsList, )
from django.views.decorators.cache import cache_page


urlpatterns = [
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   #path('', cache_page(10*1)(PostList.as_view())),
   path('', PostList.as_view()),
   path('<int:pk>', PostDetails.as_view(), name='post_detail'),
   path('new_create/', NewsCreate.as_view(), name='news_create'),
   path('article_create/', ArticlesCreate.as_view(), name='articles_create'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('<int:pk>/update/', ArticlesUpdate.as_view(), name='articles_update'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
   path('categories/<int:pk>', CategoryList.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('categories/<int:pk>/unsubscribe', unsubscribe, name='unsubscribe'),
   path('subscriptions/', SubscriptionsList.as_view(), name='subscriptions'),
]