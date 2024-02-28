cd NewsPaper

python manage.py shell

from news.models import *

user1 = User.objects.create_user(username='First_user')
user2 = User.objects.create_user(username='Second_user')

Author.objects.create(author_user=user1)
Author.objects.create(author_user=user2)

Category.objects.create(category_name='StarWars')
Category.objects.create(category_name='DeathMetal')
Category.objects.create(category_name='AutoRepair')
Category.objects.create(category_name='DragStar400')

author = Author.objects.get(id=1) #author для проверки создания
Post.objects.create(author_post=author, post_type='NE', post_name='Sequels in not in canon now!', post_content='123456')
Post.objects.create(author_post=author, post_type='AR', post_name='article1', post_content='1111111')
Post.objects.create(author_post=author, post_type='AR', post_name='article2', post_content='2222222')

Post.objects.create(author_post=author, post_type='NE', post_name='new 111!', post_content='123456')
Post.objects.create(author_post=author, post_type='NE', post_name='new222!', post_content='123456')
Post.objects.create(author_post=author, post_type='NE', post_name='new333!', post_content='123456')
Post.objects.create(author_post=author, post_type='NE', post_name='new444!', post_content='123456')
Post.objects.create(author_post=author, post_type='NE', post_name='new555!', post_content='123456')
Post.objects.create(author_post=author, post_type='NE', post_name='new666!', post_content='123456')
Post.objects.create(author_post=author, post_type='NE', post_name='new777!', post_content='123456')
Post.objects.create(author_post=author, post_type='NE', post_name='new888!', post_content='123456')
Post.objects.create(author_post=author, post_type='NE', post_name='new999!', post_content='123456')
Post.objects.create(author_post=author, post_type='NE', post_name='new10!', post_content='123456')

Post.objects.create(author_post=author, post_type='AR', post_name='article3', post_content='2222222')
Post.objects.create(author_post=author, post_type='AR', post_name='article4', post_content='2222222')
Post.objects.create(author_post=author, post_type='AR', post_name='article5', post_content='2222222')
Post.objects.create(author_post=author, post_type='AR', post_name='article6', post_content='2222222')
Post.objects.create(author_post=author, post_type='AR', post_name='article7', post_content='2222222')
Post.objects.create(author_post=author, post_type='AR', post_name='article8', post_content='2222222')
Post.objects.create(author_post=author, post_type='AR', post_name='article9', post_content='2222222')
Post.objects.create(author_post=author, post_type='AR', post_name='article10', post_content='2222222')
Post.objects.create(author_post=author, post_type='AR', post_name='article11', post_content='2222222')
Post.objects.create(author_post=author, post_type='AR', post_name='article12', post_content='2222222')
Post.objects.create(author_post=author, post_type='AR', post_name='article13', post_content='2222222')


Post.objects.get(id=1).post_category.add(Category.objects.get(id=1))
Post.objects.get(id=1).post_category.add(Category.objects.get(id=2))
Post.objects.get(id=2).post_category.add(Category.objects.get(id=3))
Post.objects.get(id=2).post_category.add(Category.objects.get(id=4))
Post.objects.get(id=3).post_category.add(Category.objects.get(id=2))
Post.objects.get(id=3).post_category.add(Category.objects.get(id=4))

Comment.objects.create(post=Post.objects.get(id=1), user=Author.objects.get(id=1).author_user, comment_text='comment_1')    #post и user из связей таблиц в классе комментария
Comment.objects.create(post=Post.objects.get(id=2), user=Author.objects.get(id=2).author_user, comment_text='comment_2')
Comment.objects.create(post=Post.objects.get(id=3), user=Author.objects.get(id=1).author_user, comment_text='comment_3')
Comment.objects.create(post=Post.objects.get(id=3), user=Author.objects.get(id=2).author_user, comment_text='comment_4')

Comment.objects.get(id=1).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=4).like()

Comment.objects.get(id=1).dislike()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=4).dislike()

a = Author.objects.get(id=1)
a.update_rating()
a._author_rating

b = Author.objects.get(id=2)
b.update_rating()
b._author_rating

best_user = Author.objects.order_by('-_author_rating').values('author_user', '_author_rating')[0]

best_article = Post.objects.order_by('-rating').values('author_post', 'rating', 'post_name', 'time_of_creation')[0]

best_article_preview = Post.objects.order_by('-rating')[0].preview()

all_com = Post.objects.order_by('-rating')[0].comment_set.all().values('comment_date', 'user__username', 'rating', 'comment_text')

# Post.objects.order_by('-rating')[0].comment_set.all()
#python -Xutf8 manage.py dumpdata > data.json
