#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


def is_none(x):
    if x.a is None:
        return False
    return True


def beautiful_content(url):
    text = http_get(url,"gbk")
    html = beautiful_html(text)
    return html.find(id='content').get_text()


def catalogue(url):
    text = http_get(url,"gbk")
    html = beautiful_html(text)
    cataloguelist = html.find(id='list').find_all(name ='dd')
    cataloguelist.reverse()
    cataloguelist = list(filter(is_none,cataloguelist))

    # for catalogue  in catalogueList:
    #     if catalogue.a is not None:
    #         print(catalogue.a)
    return cataloguelist[0].a.attrs['href']


def search(name):
    url = "http://zhannei.baidu.com/cse/search?q="+name+"&click=1&entry=1&s=17512219138159063592&nsid="
    text = http_get(url,"utf-8")
    html = beautiful_html(text)
    res = html.find(class_='result-game-item-pic-link')

    return res.attrs['href'];


def http_get(url,encoding):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    req = requests.get(url, headers=headers)
    req.encoding = encoding

    return req.text


def beautiful_html(text):
    return BeautifulSoup(text, "html.parser")


if __name__ == '__main__':
    name = "一念永恒"
    name = "圣墟"
    searchUrl = search(name)
    print(searchUrl)
    txtUrl = catalogue(searchUrl)
    print(txtUrl)
    print(beautiful_content(searchUrl + txtUrl).replace("笔趣阁 www.biqiuge.com，最快更新"+name+"最新章节！",''))


