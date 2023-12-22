from django import template
from django.conf import settings


register = template.Library()

f = open(f'{settings.BASE_DIR}/news/templatetags/BAD_WORDS.txt', 'r', encoding='utf8')
BAD_WORDS = tuple(f.read().lower().split("\n"))
f.close()

@register.filter()
def censored(str, tuple=BAD_WORDS):
    list_str = str.split()
    for word in tuple:
        for i in range(len(list_str)):
            while list_str[i].lower().find(word) >= 0:
                a = list_str[i].lower().find(word)
                len_word = len(word)
                if a + len_word > len(list_str[i]):
                    list_str[i] = list_str[i][:a + 1] + "*" * (len_word - 1)
                else:
                    list_str[i] = list_str[i][:a + 1] + "*" * (len_word - 1) + list_str[i][a + len_word:]
    return " ".join(list_str)




