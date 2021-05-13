from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Author, Category, Post, Comment
from .filters import NewsFilter
from .forms import NewsForm

class NewsList(ListView):
    template_name = 'flatpages/news.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через html-шаблон
    queryset = Post.objects.all().values().order_by('-id')
    paginate_by = 10

class NewsDetail(DetailView):
    template_name = 'flatpages/details.html'
    context_object_name = 'details'
    queryset = Post.objects.all().values()

class NewsSearch(ListView):
    template_name = 'flatpages/search.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через html-шаблон
    queryset = Post.objects.all().values().order_by('-id')
    paginate_by = 10
    form_class = NewsForm

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст

        context['categories'] = Post.objects.all()
        context['form'] = NewsForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)

# дженерик для создания объекта. Надо указать только имя шаблона и класс формы который мы написали в прошлом юните. Остальное он сделает за вас
class NewsCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'flatpages/post_create.html'
    form_class = NewsForm
    permission_required = ('news.add_post',)

# дженерик для редактирования объекта
class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'flatpages/post_create.html'
    form_class = NewsForm
    permission_required = ('news.change_post',)

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

   # @method_decorator(login_required(login_url='/news'))
    #class ProtectedView(LoginRequiredMixin, TemplateView):
       # template_name = 'protected_page.html'


# дженерик для удаления товара
class NewsDeleteView(DeleteView):
    template_name = 'flatpages/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

class KabinetView(LoginRequiredMixin, TemplateView):
    template_name = 'flatpages/kabinet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context












