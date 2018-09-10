# -*- coding: utf-8 -*-

import urllib.request
import urllib.response
from bs4 import BeautifulSoup
import re
import json
import os
import yaml


def requestdata(url):
    res = urllib.request.urlopen(url)
    data = res.read()
    res.close()
    return json.loads(data)

def nextpageurl(data):
    return data["paging"]["next"]


def picurl(picURLList, data):
    for content in data["data"]:
        soup = BeautifulSoup(content['content'], 'html.parser')
        for img in soup.find_all('img'):
            match = re.match('https://.*', img.get('src'))
            if match:
                picURLList.append(match.group(0))
    return picURLList


def savepic(dir, picUrl):
    if not os.path.exists(dir):
        os.mkdir(dir)
    file = dir + picUrl.split("/")[-1]
    if os.path.exists(file):
        return
    res = urllib.request.urlopen(picUrl)
    r = open(file, "wb")
    r.write(res.read())
    print("下载一张照片成功！" + picUrl)


def downloadpersonpic(dir, url):
    picURLList = []
    is_end = "false"
    print("开始进行下载！")
    while is_end == "false":
        jsonData = requestdata(url)
        is_end = jsonData["paging"]["is_end"]
        picurl(picURLList, jsonData)
        for picUrl in picURLList:
            print("当前下载url: " + url)
            savepic(dir, picUrl)
        url = jsonData["paging"]["next"]
        picURLList.clear()
    print("下载结束！")

if __name__ == '__main__':
    with open("application.yml", "r") as ymlfile:
        config = yaml.load(ymlfile)
    url = config["zhihu"]["url"]
    dir = config["path"]["dir"]
    downloadpersonpic(dir, url)
