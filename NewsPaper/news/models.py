from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse, reverse_lazy


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    _author_rating = models.IntegerField(default=0, db_column='author_rating')

    def update_rating(self):
        # post_rating = self.post_set.aggregate(Sum('rating')).get('rating__sum') or 0
        # comment_rating = self.author_user.comment_set.aggregate(Sum('rating')).get('rating__sum') or 0
        # compost_rating = Comment.objects.filter(commentPost__postAuthor=self).aggregate(Sum('rating')).get('rating__sum') or 0
        #
        # self.rating = post_rating * 3 + comment_rating + compost_rating
        # self.save()

        pRating = self.post_set.aggregate(postRating=Sum('rating'))  #сбор данных поля, к которому применяется функция
        pRat = 0
        pRat += pRating.get('postRating')

        cRating = self.author_user.comment_set.aggregate(commentRating=Sum('rating')) #замена цикла for
        cRat = 0
        cRat += cRating.get('commentRating')

        self._author_rating = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name.title()


class Post(models.Model):
    author_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_category = models.ManyToManyField(Category, through='PostCategory')

    NEWS = 'NE'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )

    post_type = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    post_name = models.CharField(max_length=255)
    post_content = models.TextField()
    rating = models.IntegerField(default=0)
    time_of_creation = models.DateTimeField(auto_now_add=True)

    def preview(self):
        return f'{self.post_content[0:123]}...'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return self.post_name.title()

    def get_absolute_url(self): #для открытия страницы после создания товара
        return reverse_lazy('post_detail', kwargs={'pk': self.pk})


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.title()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


