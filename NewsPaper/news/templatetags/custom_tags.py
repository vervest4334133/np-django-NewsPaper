from django import template


register = template.Library()

@register.simple_tag(takes_context=True)  #сообщает Django, что для работы тега требуется передать контекст. Именно тот контекст, который мы редактировали.
def url_replace(context, **kwargs): #тег для сохранения заполнения формы поиска
   d = context['request'].GET.copy()  #позволяет скопировать все параметры текущего запроса.
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()