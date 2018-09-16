# coding utf-8
from litte_spider import UrlManager, HtmlDownloader, HtmlParser, HtmlOutputer
'''
    爬虫调用模块
'''
'''
______________________________________________________
target: 百度搜索风云榜
urls:
    实时热点 http://top.baidu.com/buzz?b=1&c=513
    今日热点 http://top.baidu.com/buzz?b=341&c=513
    七日热点 http://top.baidu.com/buzz?b=42&c=513
    民生热点 http://top.baidu.com/buzz?b=342&c=513
    娱乐热点 http://top.baidu.com/buzz?b=344&c=513
    体育热点 http://top.baidu.com/buzz?b=11&c=513
______________________________________________________
target: 微博热搜
urls:
    热搜榜 http://s.weibo.com/top/summary?cate=realtimehot
______________________________________________________
target: SegmentFault 思否
urls:
    区块链 https://segmentfault.com/bc
    人工智能 https://segmentfault.com/ai
    前端 https://segmentfault.com/frontend
    后端 https://segmentfault.com/backend
    安卓 https://segmentfault.com/android
    IOS https://segmentfault.com/ios
    工具 https://segmentfault.com/toolkit
    安全 https://segmentfault.com/netsec
    程序员 https://segmentfault.com/programmer
    行业 https://segmentfault.com/industry
    标签 https://segmentfault.com/tags
'''


class SpiderMain(object):
    # 初始化
    def __init__(self, target):
        self.target = target
        self.url_manager = UrlManager.UrlManager()
        self.downloader = HtmlDownloader.HtmlDownloader()
        self.parser = HtmlParser.HtmlParser(self.target)
        self.outputer = HtmlOutputer.HtmlOutput()
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
                            Chrome/54.0.2840.100 Safari/537.36"
        }

    '''
        爬虫入口函数：craw
        :param root_urls: 入口url (list)
        :param target: 目标网站
        :return:None
    '''
    def craw(self, root_urls, decode='utf-8'):
        if '百度' in self.target or '新浪' in self.target or '思否' in self.target:
            for url in root_urls:
                try:
                    self.url_manager.add_url(url)
                    url = self.url_manager.get_url()
                    print('start crawling:', url)
                    html_content = self.downloader.download(url)
                    urls, data = self.parser.parse(url, html_content, decode)
                    self.outputer.collect_data(data)
                except Exception as e:
                    print('craw failed!', str(e))
                print('successfully!', '\n')
            return self.outputer.output_html(self.target[0])

        # elif...
        else:
            pass


# 爬百度
def craw_baidu():
    root_urls = ['http://top.baidu.com/buzz?b=1&c=513',
                 'http://top.baidu.com/buzz?b=341&c=513',
                 'http://top.baidu.com/buzz?b=42&c=513',
                 'http://top.baidu.com/buzz?b=342&c=513',
                 'http://top.baidu.com/buzz?b=344&c=513',
                 'http://top.baidu.com/buzz?b=11&c=513',
                 ]
    spider = SpiderMain(['百度', ])
    spider.craw(root_urls, 'gb18030')      # 国内网站编码通吃gb18030


# 爬新浪
def craw_xinlang():
    root_urls = ['http://s.weibo.com/top/summary?cate=realtimehot', ]
    spider = SpiderMain(['新浪', ])
    return spider.craw(root_urls, 'utf-8')


# 思否，还剩tags标签页的爬取！！！
def craw_segmentfault():
    root_urls = ['https://segmentfault.com/tags',
                 'https://segmentfault.com/bc',
                 'https://segmentfault.com/ai',
                 'https://segmentfault.com/frontend',
                 'https://segmentfault.com/backend',
                 'https://segmentfault.com/android',
                 'https://segmentfault.com/ios',
                 'https://segmentfault.com/toolkit',
                 'https://segmentfault.com/netsec',
                 'https://segmentfault.com/programmer',
                 'https://segmentfault.com/industry',
                 ]
    spider = SpiderMain(['思否', '思否标签'])
    return spider.craw(root_urls, 'utf-8')


#
def s():
    pass


if __name__ == '__main__':
    # craw_baidu()
    # craw_xinlang() 有点问题：微博页面的内容是js动态加载的！！！需要补一点只是
    craw_segmentfault()
    pass
