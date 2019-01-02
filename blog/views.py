from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post, Tag
from .utils import ObjectDetailMixin
from .forms import TagForm
# Create your views here.


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


#  Обьявил миксин, который рендерит шаблон, аналогичная функция используется и для TagDetail,
# важен порядок наследования, при наложении значений происходит переопределение
class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


# создание тега это отрисовка формы и запись в базу,реализованы вункции get, post
class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag) # меняет последнюю ветку адреса на значение
        return render(request, 'blog/tag_create.html', context={'form': bound_form})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})
