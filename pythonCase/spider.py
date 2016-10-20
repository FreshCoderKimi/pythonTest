'''
Created on 2016年10月20日                @author: ljj
小爬虫：获取某网页的所有图片
'''

#!/usr/bin/python3
#!/usr/bin/python3
import re
import urllib.request as request


def getHtml(url):
    page=request.urlopen(url)
    html=page.read()
    return html

def getImg(html):
    reg=r'src="(.*?\.jpg)" style='
    imgre=re.compile(reg)
    imglist=imgre.findall(html.decode())
    x=0
    for imgurl in imglist:
        request.urlretrieve(imgurl,"%s.jpg"%x)
        x+=1
html=getHtml("http://news.ifeng.com/a/20161020/50129325_0.shtml?_zbs_baidu_news")
getImg(html)
