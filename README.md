## ZhiHuPicDownload
----------

#### 介绍

使用python编写了一款专门用于知乎图片下载的小工具。
目前支持的功能有：
- 基于给定的url，下载话题下所有用户回答贴图
- 基于给定的url，下载用户所有回答贴图

#### 安装

python version = 3.7.0

library :	
```
urllib.request
urllib.response
bs4
re
json
os
yaml
```

#### 使用

修改 application.yml 配置项，其中 path.dir 为下载图片保存路径；zhihu.url 需要手动在知乎话题和个人页面下获取，获取方式如下：

- 知乎话题

点击话题主页，查看浏览器请求信息，关注 answers? 这条请求，拷贝request url替换掉zhihu.url
![](http://t1.aixinxi.net/o_1cn147gtj1tik9hr1n5p1vu81ceaa.png-j.jpg)

- 个人主页

进入个人主页，点击回答，查看浏览器请求信息，关注answers? 这条请求，拷贝request url替换zhihu.url
![](http://t1.aixinxi.net/o_1cn149i5u1tujcm4j7mv49765a.png-j.jpg)

配置好 application.yml后，直接使用 python 运行即可
```
$ python PersionoPic.py
```

#### 时效

截止2018/9/10，上述方式仍然可以download

如有疑问，请联系 wenpingxu123@163.com
    
    