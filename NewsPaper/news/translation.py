from .models import *
from modeltranslation.translator import register, TranslationOptions # импортируем декоратор для перевода и класс настроек, от которого будем наследоваться


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)  # указываем, какие именно поля надо переводить в виде кортежа


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('post_name', 'post_type', 'post_content')


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('comment_text',)