# !/usr/bin python
#--*-- coding:utf-8 --*--
import os
import urllib
import re
import time
import sys


url = ""
gldir = "";

 
def getHtml(url):
    file = urllib.urlopen(url)
    html = (file.read())
    return html
 
def getImageList(html):
    #reg = "http:*?\.jpg"
    reg = 'http[^"}]*?(?:\.jpg|\.png|\.jpeg)'
    imgre = re.compile(reg)
    imgList = re.findall(imgre,html)
    return imgList
 
def printImageList(imgList):
    with open(gldir + "/url.txt","wb+") as f:
       for i in imgList:
            #print i
            f.write(i+"\r\n")
 
def download(imgList, page):
    x = 1
    for imgurl in imgList:
        print 'Download '+imgurl
        if imgurl.rfind(".png") != -1:
            urllib.urlretrieve(imgurl,'%s/%s_%s.png'%(gldir,page,x))
        elif imgurl.rfind(".jpg") != -1:
            urllib.urlretrieve(imgurl,'%s/%s_%s.jpg'%(gldir,page,x))
        elif imgurl.rfind(".jpeg") != -1:
            urllib.urlretrieve(imgurl,'%s/%s_%s.jpeg'%(gldir,page,x))
        elif imgurl.rfind(".gif") != -1:
            urllib.urlretrieve(imgurl,'%s/%s_%s.gif'%(gldir,page,x))
        x+=1
    print 'Download file '+ str(x)+ ' fiel\'s end'
 
 
def downImageNum(pagenum):
    page = 1
    pageNumber = pagenum
    while(page <= pageNumber):
        html = getHtml(url)#获得url指向的html内容
        imageList = getImageList(html)
        printImageList(imageList)#打印所有的图片的地址
        download(imageList,page)#下载所有的图片
        page = page+1
 
if __name__ == '__main__':
    url = raw_input("enter the web page\n URL:")
    folder = url
    folder = folder.replace("http://","")
    folder = folder.replace("https://","")
    folder = folder.replace("/","")
    gldir = sys.path[0] + "/" + folder
    os.system('mkdir ' + gldir)
    downImageNum(1)
    time.sleep(10)
