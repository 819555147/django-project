from django.shortcuts import render, redirect
from .models import AlgorithmArticle
# Create your views here.


# 博客首页
def index(request):
    return render(request, 'blog.html')


# 算法与数据结构页面
def algorithm(request):
    articles = AlgorithmArticle.objects.filter(Tag='algorithm')
    return render(request, 'algorithm.html', {'articles': articles})


# 语言页面
def language(request):
    articles = AlgorithmArticle.objects.filter(Tag='language')
    return render(request, 'language.html', {'articles': articles})


# 编程页面
def program(request):
    articles = AlgorithmArticle.objects.filter(Tag='program')
    return render(request, 'program.html', {'articles': articles})


# 项目页面
def project(request):
    articles = AlgorithmArticle.objects.filter(Tag='project')
    return render(request, 'project.html', {'articles': articles})


# 文本编辑器
def editor(request):
    kiss = request.GET.get('kiss')
    title = request.GET.get('title')
    obj = AlgorithmArticle.objects.filter(Title=title)
    if kiss == 'fxd':
        # print({'article': obj})
        if obj is None:
            return render(request, 'page_editor.html')
        else:
            return render(request, 'page_editor.html', {'article': obj})
    else:
        return redirect('/')


# 文章处理函数
def process(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    tag = request.POST.get('tag')
    old_title = request.POST.get('old_title')

    obj = AlgorithmArticle.objects.filter(Title=old_title)

    print('呵呵', obj, obj.exists())
    if not obj.exists():  # 新文章
        AlgorithmArticle.objects.create(Title=title, Content=content, Tag=tag)
    else:  # 原有文章
        obj.update(Title=title, Content=content, Tag=tag)
    return redirect('/')


def delete(request):
    title = request.POST.get('delete_title')
    print(title)    # 有问题，这里的title获取老失败，得到一个None!!!
    AlgorithmArticle.objects.filter(Title=title).delete()
    return redirect('/')
