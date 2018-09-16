# coding utf-8
'''
url 管理器
'''


class UrlManager(object):
    def __init__(self):
        self.old_set = set()
        self.new_set = set()

    # 添加一条新的url(未爬过且不存在于new_set中)
    def add_url(self, url):
        if url is None:
            return
        if url not in self.old_set and url not in self.new_set:
            self.new_set.add(url)

    # 添加新的urls
    def add_urls(self, urls):
        if urls is None and len(urls) == 0:
            return None
        for url in urls:
            self.add_url(url)

    # 判断是否还有url未爬
    def has_next_url(self):
        return len(self.new_set) != 0

    # 获取一条未爬取的url
    def get_url(self):
        if self.has_next_url():
            url = self.new_set.pop()
            self.old_set.add(url)
            return url
        return None

    # old_set存入数据库
    def store(self):
        pass
