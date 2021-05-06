from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Author, Category, Post, Comment


# создаём фильтр
class NewsFilter(FilterSet):
    class Meta:
        model = Post
        fields = ('author_post', 'post_heading', 'post_create_date')
