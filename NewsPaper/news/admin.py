from django.contrib import admin
from .models import *


# напишем уже знакомую нам функцию обнуления товара на складе
def nullfy_rating(modeladmin, request, queryset): # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(rating=0)

    nullfy_rating.short_description = 'Обнулить рейтинг' # описание для более понятного представления в админ панеле задаётся, как будто это объект


# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    # list_display = [field.name for field in Post._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения
    list_display = ('post_name', 'author_post', 'time_of_creation', 'rating')
    list_filter = ('post_name', 'post_category', 'author_post', 'time_of_creation', 'rating')
    search_fields = ('post_name', 'post_category__category_name')
    actions = [nullfy_rating]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    list_filter = ['category_name']
    search_fields = ['category_name']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_user', '_author_rating')
    list_filter = ('author_user', '_author_rating')
    search_fields = ('author_user', '_author_rating')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'user', 'comment_date', 'rating')
    list_filter = ('comment_text', 'user', 'comment_date', 'rating')
    search_fields = ('comment_text', 'user', 'comment_date')


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('post', 'category')
    list_filter = ('post', 'category')
    search_fields = ('post', 'category')


admin.site.register(Post, PostAdmin) #При регистрации вторым аргументом указывать класс модель-админа
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)