import django_filters
from django import forms

from .models import *


class PostFilter(django_filters.FilterSet):
    # time_of_creation = django_filters.DateTimeFilter('time_of_creation', label=('Created'), widget=forms.DateTimeInput())
    time_in = django_filters.DateTimeFilter(
        label='Post was created:',
        field_name='time_of_creation',
        lookup_expr='gt',
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        # В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели будет производиться фильтрация.
        fields = {
            # поиск по названию
            'post_name': ['icontains'],
            'time_of_creation': [],
            'post_category': ['exact'],
            'rating': [
                'lt',  # рейтинг должен быть меньше или равна указанной
                'gt',  # рейтинг должен быть больше или равна указанной
            ],
        }



# class CustomerOrderFilter(django_filters.FilterSet):
#     product = django_filters.ChoiceFilter(
#         # replace choices with the choices defined in your order model or just copy it over
#         choices=<PRODUCT_CHOICES>,
#         widget=forms.Select(attrs={'class': 'form-control'}))