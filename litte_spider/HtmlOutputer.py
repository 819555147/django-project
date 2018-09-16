# coding utf-8
'''
    网页输出器
'''
import codecs
import time
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spider.settings")
django.setup()

from spider_site.models import BaiDu, SegmentFault


class HtmlOutput(object):
    def __init__(self):
        # 存储数据
        self.datas = []

    # 收集数据
    def collect_data(self, data):
        if data is None:
            return
        else:
            self.datas.append(data)

    # 输出数据
    def output_html(self, target):
        ISO_TIME_FORMAT = '%Y-%m-%d'
        output = '''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
                    <meta name="keyword" content="Spider output HTML">
                    <meta name="author" content="Richard Lee">
                    <meta name="digest" content="">
                    <meta name="gratitude" content="to BaiDu">
                    <link rel="stylesheet" type="text/css" href="">
                    <title>查询结果</title>
                    <style>
                        * { margin:0;padding:0; }
                        div { margin:0 auto;padding:40px; }
                        h1 { padding:0 0 40px 20px;text-align:center; }
                        table { width:80%;margin:auto;}
                        td,th { text-align:center;padding:10px;}
                    </style>    
                </head>
                <body>
                <a href="{% url 'MySpider:index' %}#spider" target='_blank' style="display:block;width:100px;
                text-align:center;margin:auto;">
                回到爬虫
                </a>
                '''
        filename = './spider_site/templates/' + target + '-' + \
                   time.strftime(ISO_TIME_FORMAT, time.localtime(time.time())) + ".html"
        if '百度' in target:
            try:
                # print(self.datas)
                # print(len(self.datas))

                # 存数据库
                # 存文件，关于文件还需要有一个完善的方案，是否是输出到用户的本地磁盘上？？
                with codecs.open(filename, "w", "utf-8") as f:
                    # 输出网页源代码！！！ 放一个导航栏！！！直接重用先前的那个!!
                    count = 1
                    for data in self.datas:
                        output += '<div' + ' class="' + 'div' + str(count) + '">'
                        output += '<h1>' + data["model_name"] + '</h1>'
                        output += '<table border="1">'
                        output += '<tr><th>关键字</th><th>链接<th><th>热度</th></tr>'
                        for i in range(len(data["title"])):
                            # 存入数据库，注意对之前已存入的数据的处理
                            temp = BaiDu.objects.filter(Keyword=data['title'][i])   # 返回一个<QuerySet [...]>
                            if len(temp) is not 0:  # 若已存在相应数据，更新SearchHeat
                                for ob in temp:
                                    ob.SearchHeat = data['search_heat'][i]
                                    ob.save()
                            else:  # 不存在相应数据，则生成
                                BaiDu.objects.create(Keyword=data['title'][i], Link=data['link'][i],
                                                     SearchHeat=data['search_heat'][i], Content='null')

                            output += '<tr>'
                            output += '<td><span>' + data["title"][i] + '</span></td>'
                            output += '<td><a' + ' href="' + data["link"][i] + '" target="_blank">' + '查看</a><td>'
                            output += '<td><span>' + data["search_heat"][i] + '</span></td>'
                            output += '</tr>'
                        output += '</table>'
                        output += '</div>'
                        count += 1
                    output += '</body></html>'
                    f.write(output)
                    return output
            except Exception as e:
                print("Error happened when run HtmlOutputer: ", str(e))
                # ...异常处理？？？

        elif '思否' in target:
            try:
                with codecs.open(filename, "w+", "utf-8") as f:
                    count = 0
                    model_name = ['标签树', '区块链', '人工智能', '前端', '后端',
                                  'Android', 'ios', '工具', '安全', '程序员', '行业']
                    for data in self.datas:
                        output += '<div' + ' class="' + 'div' + str(count) + '">'
                        output += '<h1>' + model_name[count] + '</h1>'
                        output += '<table border="1">'
                        output += '<tr><th>关键字</th><th>链接</th><th>作者</th><th>标签-时间</th></tr>'
                        for i in range(len(data["title"])):
                            '''# 存入数据库，注意对之前已存入的数据的处理
                            temp = SegmentFault.objects.filter(Item=data['title'][i], Author=data['author']['name'][i])
                            # filter返回一个<QuerySet [...]>
                            if len(temp) is not 0:  # 若已存在相应数据，不做操作
                                continue  # do nothing
                            else:  # 不存在相应数据，则生成
                                SegmentFault.objects.create(Item=data['title'][i], Link=data['link'][i],
                                                            Author=data['author']['name'][i],
                                                            AuthorLink=data['author']['link'][i],
                                                            Tag=data["tags"][i], Content='null')
                            '''
                            output += '<tr>'
                            output += '<td>' + data["title"][i] + '</td>'
                            output += '<td><a href="' + data["link"][i] + '">查看</a></td>'
                            output += '<td><a href="' + data["author"]["link"][i] + '">' + \
                                      data["author"]["name"][i] + '</a></td>'
                            output += '<td>' + data["tags"][i] + data["date"][i] + '</td>'
                            output += '</tr>'
                        output += '</table>'
                        output += '</div>'
                        count += 1
                    output += '</body></html>'
                    f.write(output)
            except Exception as e:
                print("Error happened when run HtmlOutputer: ", str(e))
                # ...异常处理？？？
            return output
        # elif...
        else:
            pass


if __name__ == '__main__':

    tep = BaiDu.objects.filter(Keyword='asssda')
    print(len(tep))
    if len(tep) is not 0:
        for o in tep:
            o.SearchHeat = 112121000
            o.save()
    else:
        BaiDu.objects.create(Keyword='sad', Link='asdas', SearchHeat=344242, Content='null')