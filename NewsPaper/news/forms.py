from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class NewsForm(forms.ModelForm):
   class Meta:
       model = Post
       # fields = '__all__'
       fields = [
           'post_name',
           # 'post_type',
           'post_content',
           'post_category',
           'author_post',
       ]

   def clean(self):
       cleaned_data = super().clean()
       post_content = cleaned_data.get("post_content")
       if post_content is not None and len(post_content) < 5:
           raise ValidationError({
               "post_content": "Содержание публикации не может быть менее 5 символов."
           })

       return cleaned_data


   def clean_name(self):
       post_name = self.cleaned_data["post_name"]
       if post_name[0].islower():
           raise ValidationError(
               "Название должно начинаться с заглавной буквы"
           )

       return post_name


class ArticlesForm(forms.ModelForm):
   class Meta:
       model = Post
       # fields = '__all__'
       fields = [
           'post_name',
           # 'post_type',
           'post_content',
           'post_category',
           'author_post',
       ]

   def clean(self):
       cleaned_data = super().clean()
       post_content = cleaned_data.get("post_content")
       if post_content is not None and len(post_content) < 5:
           raise ValidationError({
               "post_content": "Содержание публикации не может быть менее 5 символов."
           })

       return cleaned_data


   def clean_name(self):
       post_name = self.cleaned_data["post_name"]
       if post_name[0].islower():
           raise ValidationError(
               "Название должно начинаться с заглавной буквы"
           )

       return post_name