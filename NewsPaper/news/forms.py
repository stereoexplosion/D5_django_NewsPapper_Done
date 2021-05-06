from django.forms import ModelForm
from .models import Author, Category, Post, Comment


# Создаём модельную форму
class NewsForm(ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['author_post', 'post_heading', 'post_type_select', 'post_text', 'post_category']