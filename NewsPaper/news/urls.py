from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, NewsCreateView, NewsUpdateView, NewsDeleteView  # импортируем наше представление



urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='details'),
    path('search', NewsSearch.as_view()),
    path('post_create', NewsCreateView.as_view(), name='create'),
    path('<int:pk>/edit', NewsUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='delete'),
    # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
]