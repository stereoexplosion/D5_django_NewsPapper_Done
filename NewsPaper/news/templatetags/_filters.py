from django import template

register = template.Library()  # если мы не зарегестрируем наши фильтры, то django никогда не узнает где именно их искать и фильтры потеряются(

@register.filter(name='censor')
def censor(value):
    arg = ['пидор', 'сука', 'ниггер']
    b = value.split(' ')
    for c in arg:
        for a in b:
            if a == c:
                b.remove(a)
    return ' '.join(b)


