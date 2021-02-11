from django.views.generic import ListView, DetailView

from .models import Author, Category, Post, Comment
from django.shortcuts import render, get_object_or_404


class NewsList(ListView):
    template_name = 'flatpages/news.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через html-шаблон
    queryset = Post.objects.all().values().order_by('-id')

class NewsDetail(DetailView):
    template_name = 'flatpages/details.html'
    context_object_name = 'details'
    queryset = Post.objects.all().values()








