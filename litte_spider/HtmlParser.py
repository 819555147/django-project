# coding utf-8
'''
Html源码解析器，提取需要的信息，针对不同网站需要定制
'''
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class HtmlParser(object):
    #
    def __init__(self, target):
        self.target = target

    # 获取源码中所有url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        return new_urls

    # 获取源码中的内容，参数->{ page_url:, soup: beautifulSoup对象}
    # return a dict, include some lists
    def _get_new_data(self, page_url, soup):
        # 针对百度搜索风云榜的解析方式
        if '百度' in self.target:
            # 结果集
            title = []
            link = []
            search_heat = []
            res_data = {"title": title, "link": link, "search_heat": search_heat}

            try:
                # 目标：<td class="keyword"><a class="list-title" href="想要的链接">想要的内容</a></td>
                a_nodes = soup.find_all("a", class_="list-title")
                sh_nodes = soup.find_all("td", class_="last")

                # 目标：正则表达式匹配每一模块标题，<a class="(或者有多个类名) se">模块名</a>
                item_node = soup.find("a", class_=re.compile(r"^se$|.*\s+se.*"))
                res_data["model_name"] = item_node.get_text()
                print(res_data["model_name"])

                for node in a_nodes:
                    res_data["title"].append(node.get_text())
                    res_data["link"].append(node["href"])
                for node in sh_nodes:
                    res_data["search_heat"].append(node.get_text())
            except Exception as e:
                print('Error happened when run HtmlParser:', str(e))
            return res_data

        # 针对思否的解析方法
        elif '思否' in self.target:
            # 结果集
            title = []
            tags = []
            link = []
            ar_name = []
            ar_link = []
            author = {"name": ar_name, "link": ar_link}
            date = []
            res_data = {"title": title, "link": link, "tags": tags, "author": author, "date": date}
            try:
                # 目标 <h4 class="news__item-title mt0"><a class="mr10" target="_blank" href="目标link">目标标题 \
                # </a></h4>
                # 目标<ul class="taglist--inline ib"><li class="tagPopup"><a class="tag" href="无用link">目标tag
                # </a></li></ul>
                # 目标 <p class="news__item-meta"><a></a> \
                # <a class="" href="目标link">目标author</a><span></span><span>目标date</span></p>
                title_link_nodes = soup.find_all("a", class_="mr10", target="_blank")
                tags_ul_nodes = soup.find_all("ul", class_="taglist--inline ib")
                author_date_p_nodes = soup.find_all("p", class_="news__item-meta")
                for node in title_link_nodes:
                    res_data["title"].append(node.get_text())
                    res_data["link"].append(urljoin('https://segmentfault.com/', node["href"]))
                for node in tags_ul_nodes:
                    tag_str = ''
                    for a_child in node.children:
                        tag_str += str.strip(a_child.get_text()) + ' '
                    res_data["tags"].append(tag_str)
                for node in author_date_p_nodes:
                    child = node.children
                    next(child)
                    temp_node = next(child)
                    res_data["author"]["name"].append(temp_node.get_text())
                    res_data["author"]["link"].append(urljoin('https://segmentfault.com/', temp_node["href"]))
                    next(child)
                    res_data["date"].append(next(child).get_text())
                # print(res_data)
            except Exception as e:
                print('Error happened when run HtmlParser:', str(e))

            return res_data

        else:
            pass

    # 解析方法，参数->{ page_url:目标网页, html_content:目标网页源代码}
    def parse(self, page_url, html_content, encoding):
        if page_url is None or HtmlParser is None:
            return
        # soup对象
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding=encoding)
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
