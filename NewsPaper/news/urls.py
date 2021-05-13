from django.urls import path, include
from .views import NewsList, NewsDetail, NewsSearch, NewsCreateView, NewsUpdateView, NewsDeleteView, KabinetView  # импортируем наше представление
from django.contrib import admin




urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='details'),
    path('search', NewsSearch.as_view()),
    path('post_create', NewsCreateView.as_view(), name='create'),
    path('<int:pk>/edit', NewsUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='delete'),
    path('admin/', admin.site.urls),
    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    path('kabinet', KabinetView.as_view()),
    # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
]