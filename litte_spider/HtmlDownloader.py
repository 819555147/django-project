# coding utf-8
'''
网页下载器，下载网页源代码，即获取httpResponse
'''
import requests
from http import cookiejar


class HtmlDownloader(object):
    # 网页下载并返回
    # 参数->{url:目标网页, method:请求方式, retry_count:失败重试次数, header:http请求头, proxy:代理, data:http请求body表单数据 }
    def download(self, url, retry_count=3, header=None, proxy=None, data=None):
        if url is None:
            return
        try:
            if data is not None:
                r = requests.post(url, data=data)
            else:
                r = requests.get(url)
            '''
            搁置
            proxy
            cookie
            '''
            content = r.content
            # print(r.text)
        except Exception as e:
            print('Html Downloader Error: ', str(e))
            content = None
            # 递归终止条件
            if retry_count > 0:
                if hasattr(r, 'status_code') and 500 < r.status_code < 600:
                    # 服务器错误，可再次尝试下载
                    return self.download(url, retry_count-1, header, proxy, data)
        return content

