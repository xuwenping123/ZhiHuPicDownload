import urllib.request
import urllib.response
from bs4 import BeautifulSoup
import re
import json
import os

def requestData(url):
    res = urllib.request.urlopen(url)
    data = res.read()
    return json.loads(data)

def requestNextURL(data):
    return data["paging"]["next"]

def requestPicURL(picURLList, data):
    for content in data["data"]:
        soup = BeautifulSoup(content['content'], 'html.parser')
        for img in soup.find_all('img'):
            match = re.match('https://.*', img.get('src'))
            if match:
                picURLList.append(match.group(0))
    return picURLList

def savePic(dir, picUrl):
    if not os.path.exists(dir):
        os.mkdir(dir)
    file = dir + picUrl.split("/")[-1]
    if os.path.exists(file):
        return
    res = urllib.request.urlopen(picUrl)
    r = open(file, "wb")
    r.write(res.read())
    print("下载一张照片成功！" + picUrl)

def downloadPersonPic(dir, url):
    picURLList = []
    while True:
        jsonData = requestData(url)
        print("开始进行下载！")
        print("下一页", jsonData["paging"]["next"])
        print("offset=0" not in jsonData["paging"]["next"])
        if "offset=0" not in jsonData["paging"]["next"]:
            requestPicURL(picURLList, jsonData)
            for picUrl in picURLList:
                savePic(dir, picUrl)
            url = jsonData["paging"]["next"]
            picURLList.clear()
        else:
            break


if __name__ == '__main__':
    url = "https://www.zhihu.com/api/v4/members/mo-chi-78-6/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cvoting%2Cis_author%2Cis_thanked%2Cis_nothelp%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20&sort_by=created"
    dir = "E:/zhihu_pic/3/"
    print("开始运行！")
    downloadPersonPic(dir, url)
    print("下载完成！")
