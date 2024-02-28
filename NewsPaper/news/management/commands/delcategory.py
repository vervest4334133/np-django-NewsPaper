from django.core.management.base import BaseCommand, CommandError
from news.models import *


class Command(BaseCommand):
    help = 'Удалить публикации в данной категории?'  # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    requires_migrations_checks = True  # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        # здесь можете писать любой код, который выполнется при вызове вашей команды
        # self.stdout.readable()
        # self.stdout.write(
        #     'Do you really want to deleted posts in selected category? yes/no')  # спрашиваем пользователя действительно ли он хочет удалить все товары
        # answer = input()  # считываем подтверждение
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no')

        # if answer == 'yes':  # в случае подтверждения действительно удаляем все товары
        #     category = Category.objects.get(category_name=options['category'])
        #     Post.objects.filter(post_category=category).delete()
        #     self.stdout.write(self.style.SUCCESS('Succesfully deleted posts in selected category!'))
        #     return
        #
        # self.stdout.write(
        #     self.style.ERROR('Access denied'))  # в случае неправильного подтверждения, говорим что в доступе отказано

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return

        try:
            category = Category.objects.get(category_name=options['category'])
            Post.objects.filter(post_category=category).delete()
            self.stdout.write(self.style.SUCCESS(
                f'Succesfully deleted all news from category "{category.category_name}"'))  # в случае неправильного подтверждения говорим, что в доступе отказано

        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category'))