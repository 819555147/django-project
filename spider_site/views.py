from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.db import models
from django.forms.models import model_to_dict
from spider_site.models import *
import time
import os
from litte_spider.SpiderMain import craw_segmentfault, craw_baidu
import re
import random
'''
编写响应函数
'''
# Create your views here.


# 获取图像名称列表 参数：路径，图片类型，数量
def get_img_list(path, photos, number):
    # 一次只能获取最多100张图片
    number = int(number)
    number = 100 if number > 100 else number
    files = os.listdir(path)
    imgs = []
    for file in files:
        # 用户所需图片数少于已有图片数
        if len(imgs) == number*2:
            break
        name, ext = os.path.splitext(file)
        ext = str(ext).lower()
        if ext == '.jpg' or ext == '.jpeg' or ext == '.png':
            imgs.append('./images/pexels/thumbnail/' + photos + '/' + file)
    # 最后返回的图片可能不够
    return imgs


# 检查是否有所需图片
def check_photos(photos):
    # 检查该类型图片是否存在。。。。。
    # 需要同义词匹配。。。但是。。。目前只能。。。呵呵呵
    files = os.listdir(r'./static/images/pexels/thumbnail')
    if photos in files:
        return True
    else:
        return False


# 调度函数，给定爬取目标，返回结果页面和数据信息
def manage(request, target):
    ISO_TIME_FORMAT = '%Y-%m-%d'

    if str(target) == '百度热搜':
        craw_baidu()
        pagename = '百度' + '-' + time.strftime(ISO_TIME_FORMAT, time.localtime(time.time())) + ".html"
        meta = None

    elif str(target) == 'SegmentFault':
        craw_segmentfault()
        pagename = '思否' + '-' + time.strftime(ISO_TIME_FORMAT, time.localtime(time.time())) + ".html"
        meta = None

    elif str(target) == 'SegmentFault_Full':
        pagename = 'SegmentFault_Full.html'
        low = random.randrange(1, 9400)
        high = low + 200
        sf = segmentfaultfull.objects.all()
        data = list(sf)[low:high+1]
        meta = {'data': data, 'len': len(sf), 'num': 200}

    elif str(target) == '起点中文网':
        pagename = 'books.html'
        books = os.listdir(r'./static/books')
        # map(lambda b: , books)
        meta = {'books': books}

    elif str(target) == '虎嗅网':
        # pagename = '虎嗅' + time.strftime(ISO_TIME_FORMAT, time.localtime(time.time())) + ".html"
        huxiu = os.listdir('./static/huxiu')
        huxiu = huxiu[-1]
        with open('./static/huxiu/' + huxiu, 'r', encoding='utf-8') as f:
            html = f.read()
        html = re.findall("<body>(.*?)</body>", html, re.S)[0]
        pagename = 'huxiu.html'
        html = str(html).replace('"', '\\"')
        html = html.replace("\n", "\\")
        meta = {'html': html}

    elif str(target) == '豆瓣电影排行':
        pagename = 'top250.txt'
        meta = None

    elif str(target) == 'Pexels':
        nums = int(request.POST.get('crawl_target_photos_num', 'Nothing'))
        photos = request.POST.get('crawl_target_photos', 'Nothing')
        # 进行筛选，看一看photos给出的照片有没有！

        if check_photos(photos) is True:
            path = r'./static/images/pexels/thumbnail/' + photos
            imgs = get_img_list(path, photos, nums)
            for img in imgs:
                img += './images/pexels/thumbnail/' + photos + '/'
            pagename = "photos.html"
            meta = {'nums': nums if nums < len(imgs) else len(imgs), 'photos': photos, 'imgs': imgs[:nums], 'others': imgs[nums:]}

        else:
            pagename = 'error.html'
            meta = {'message': 'Pexels_Spiser 需要时间去为您下载新的图片！你可以试着换一种图片！'}

    else:
        pagename = "aindex.html"
        meta = None

    return pagename, meta


# 主页
def index(request):
    un = request.session.get('username')
    if un:
        return render(request, 'index.html')
    else:
        return redirect('/entry/login')


# 爬虫调度
def spider_run(request):
    # 获得爬取目标
    target = request.POST.get('crawl_target', 'Nothing')

    # 未完成模块
    if str(target) == 'Nothing':
        return render(request, 'error.html', {'message': '没有爬取目标！'})  # 还没有写

    # 调度
    pagename, meta = manage(request, target)
    return render(request, pagename, meta)



# 返回百度
def get_baidu(request):
    r = requests.get('http://www.baidu.com/')
    return HttpResponse(u'<h1 style="color:#ccc;position:absolute;left:46%;top:50%;background-color:black;opacity:0.5;">\
    Hello world!</h1>'+r.content.decode('utf-8'))


def aindex(request):
    Githubs = GitHub.objects.all()
    return render(request, 'aindex.html', {'Githubs': Githubs})


def atricle_page(request, article_id):
    article = GitHub.objects.get(pk=article_id)
    return render(request, 'article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'edit_page.html')
    article = GitHub.objects.get(pk=article_id)
    return render(request, 'edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST['title']
    content = request.POST.get('content', 'default value')
    article_id = request.POST['article_id']
    if str(article_id) == '0':
        GitHub.objects.create(Item=title, Link='null', Content=content)
        article = DouBan.objects.get(pk=1)
        Githubs = GitHub.objects.all()
        return render(request, 'aindex.html', {'article': article, 'Githubs': Githubs})
    article = GitHub.objects.get(pk=article_id)
    article.Item = title
    article.Content = content
    article.save()
    return render(request, 'article_page.html', {'article': article})


def just_try(request):
    items = GitHub.objects.all()
    return render(request, 'just_try.html', {'items': items})


def jump(request, item_id):
    item = GitHub.objects.get(pk=item_id)
    return render(request, 'jump.html', {'item': item})


def get_photos(request):
    return render(request, 'photos.html')
