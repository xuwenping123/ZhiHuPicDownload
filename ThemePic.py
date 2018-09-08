import os
import urllib.request
import urllib.response
import json
import re
from bs4 import BeautifulSoup

def getRequestJson(url):
    res = urllib.request.urlopen(url)
    jsonData = json.loads(res.read())
    return jsonData

def getRequestJsonData(jsonData):
    return jsonData["data"]

def getRequestNextPageURL(jsonData):
    return jsonData["paging"]["next"]

def getRequestPreviousPageURL(jsonData):
    return jsonData["paging"]["previous"]

def getPagePicUrl(picUrlList, pageJsonData):

    for content in pageJsonData:
        soup = BeautifulSoup(content['content'], 'html.parser')
        for img in soup.find_all('img'):
            match = re.match('https://.*', img.get('src'))
            if match:
                picUrlList.append(match.group(0))
    return picUrlList

def savePic(dir, picUrl):
    if os.path.exists(dir):
      #  os.mkdir(dir)
        print(dir)
    path = picUrl.split("/")[-1]
    request = urllib.request.urlopen(picUrl)
    if os.path.exists(dir + path):
        return
    r = open(dir + path, "wb")
    r.write(request.read())
    print("下载一张照片成功！ " + picUrl)
    return

def downloadZhiHuPic(url, dir):
    picUrlList = []
    while True:
        jsonData = getRequestJson(url)
        print("开始进行下载！")
        print("下一页", jsonData["paging"]["next"])
        print("offset=0" not in jsonData["paging"]["next"])
        if "offset=0" not in jsonData["paging"]["next"]:
            pageData = getRequestJsonData(jsonData)
            getPagePicUrl(picUrlList, pageData)
            for picUrl in picUrlList:
                savePic(dir, picUrl)
            url = jsonData["paging"]["next"]
            picUrlList.clear()
        else:
            break

if __name__ == '__main__':
    url = "https://www.zhihu.com/api/v4/questions/39838691/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=&limit=3&sort_by=default"
    dir = "E:/zhihu_pic/"
    downloadZhiHuPic(url, dir)
    print("download pic end!")