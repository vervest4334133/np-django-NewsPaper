from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Comment


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


# class CommentForm(forms.ModelForm):
#    class Meta:
#        model = Comment
#        fields = [
#            'comment_text',
#        ]
#
#    def clean(self):
#        cleaned_data = super().clean()
#        comment_text = cleaned_data.get("comment_text")
#        if comment_text is not None and len(comment_text) < 5:
#            raise ValidationError({
#                "comment_text": "Содержание комментария не может быть менее 5 символов."
#            })
#
#        return cleaned_data

   # def clean_name(self):
   #     comment_text = self.cleaned_data["post_name"]
   #     if post_name[0].islower():
   #         raise ValidationError(
   #             "Название должно начинаться с заглавной буквы"
   #         )
   #
   #     return post_name