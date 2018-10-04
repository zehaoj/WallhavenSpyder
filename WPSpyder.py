#_*_ coding:utf-8 _*_
#__date__='2018-08-27'
#爬取wallhaven上的的图片，支持自定义搜索关键词，自动爬取并该关键词下所有图片并存入本地电脑。
import os
import requests
import time
from progressbar import *
from lxml import etree
from threading import Thread
import tkinter as tk

print('This software is for those who dig high-resolution wallpapers. By inputing the keyword and pages you wanna download, breathtaking(or pantsdropping LOL) pictures will be automatically downloaded to your computer. It will be located in your C:\WallPaper. Do enjoy! \n')
print('这个软件是为那些喜欢高像素壁纸的人服务的。通过输入关键词和想下载的页数，你就能将大量的高质量图片下到你的电脑中。默认存储地点是C盘下的 WallPaper 文件夹。')
print('By J.Zehao\n')
print('-h : get help(获取帮助)\n')
print('-t : get tags(获取提示标签)\n')
tf = 1
while(tf == 1):
    keyWord = input(f"{'Please input the keywords that you want to download : '}")
    if keyWord == '-h':
        print('You can input keyword(tags) to download what you like. \nThen it will show how many images are there available for you to download.\ninput how many pages you wanna download. Normally, there will be 24 pics per page.')
        print('你可以输入想下载的内容的关键词(标签)。软件将告诉你有多少张图片供下载。输入你想下载的页面数(一个页面有24张)')
    elif keyWord == '-t':
        print('Here are some exemples: (rank by popularity, * is restricted content)')
        print('这里是一些标签的例子(按热门度排行，标*的为限制级内容)')
        print('women (People)')
        print('model (People)')
        print('nature (Nature)')
        print('brunette (People)')
        print('blonde (People)')
        print('landescape (Nature)')
        print('long hair (People)')
        print('anime (Anime&Manga)')
        print('anime girls (Anime&Manga)')
        print('ass (People)*')
        print('digital art (Art&Design)')
        print('women outdoors (People)')
        print('artwork (Art&Design)')
        print('trees (Nature)')
        print('looking at viewer (People)')
        print('boobs (People)*')
        print('video games (Entertainment)')
        print('leaves (Nature)')
        print('nude (People)*')
        print('portrait (Art&Design)')
        print('depth of field (Art&Design)\n')
    else:
        tf = 0

if keyWord == 'women':
    keyWord1 = 'id:222'
elif keyWord == 'model':
    keyWord1 = 'id:424'
elif keyWord == 'nature':
    keyWord1 = 'id:37'
elif keyWord == 'brunette':
    keyWord1 = 'id:182'
elif keyWord == 'blonde':
    keyWord1 = 'id:164'
elif keyWord == 'landescape':
    keyWord1 = 'id:711'
elif keyWord == 'long hair':
    keyWord1 = 'id:169'
elif keyWord == 'anime':
    keyWord1 = 'id:1'
else:
    keyWord1 = keyWord
    
class Spider():
    #初始化参数
    def __init__(self):        
        self.headers = {#headers是请求头，"User-Agent"、"Accept"等字段可通过谷歌Chrome浏览器查找！
        "User-Agent": "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
        }
        self.proxies = {#代理ip，当网站限制ip访问时，需要切换访问ip
		"http": "http://61.178.238.122:63000",
	    }
        #filePath是自定义的，本次程序运行后创建的文件夹路径，存放各种需要下载的对象。
        self.filePath = ('C:\WallPaper\\'+ keyWord + "\\" )

    def creat_File(self):
        #新建本地的文件夹路径，用于存储网页、图片等数据！
        filePath = self.filePath
        if not os.path.exists(filePath):
            os.makedirs(filePath)

    def get_pageNum(self):
        total = ""
        url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc").format(keyWord1)
        html = requests.get(url,headers = self.headers,proxies = self.proxies)
        selector = etree.HTML(html.text)
        pageInfo = selector.xpath('//header[@class="listing-header"]/h1[1]/text()')
        string = str(pageInfo[0])
        numlist = list(filter(str.isdigit,string))
        for item in numlist:
            total += item
        totalPagenum = int(total)
        return totalPagenum

    def main_fuction(self):
        #count是总图片数，times是想下载的页面数
        self.creat_File()
        count = self.get_pageNum()
        print("We have found:{} images!".format(count))
        time.sleep(1)
        times = input(f"{'How many pages do you wanna download? (24 pics per page) '}")
        print('Cool! ', 24 * int(times), 'photos will be downloaded for you. Sit tight, have a cup of coffee. It will finish in no time.')
        print('好哒！', 24 * int(times), '张照片将很快下载到您的电脑上。稍安勿躁，很快就能下完！')
        j = 1
        times = int(times)
        start = time.time()
        widgets = ['Progress: ',Percentage(), ' ', Bar('>'),' ', Timer()]
        pbar = ProgressBar(widgets=widgets, maxval=100).start()
        cc = 0
        for i in range(times):
            pic_Urls = self.getLinks(i+1)
            threads = []
            for item in pic_Urls:
                t = Thread(target = self.download, args = [item,j])
                t.start()
                threads.append(t)
                j += 1
               
            for t in threads:
                cc += 100/(24 * times)
                if cc > 100:
                    cc = 100
                t.join() 
                pbar.update(cc)
        pbar.update(100)
        end = time.time()

    def getLinks(self,number):
        #此函数可以获取给定numvber的页面中所有图片的链接，用List形式返回
        url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc&page={}").format(keyWord1,number)
        try:
            html = requests.get(url,headers = self.headers,proxies = self.proxies)
            selector = etree.HTML(html.text)
            pic_Linklist = selector.xpath('//a[@class="jsAnchor thumb-tags-toggle tagged"]/@href')
        except Exception as e:
            print(repr(e))
        return pic_Linklist

    def download(self,url,count):
        #此函数用于图片下载。其中参数url是形如：https://alpha.wallhaven.cc/wallpaper/616442/thumbTags的网址
        #616442是图片编号，我们需要用strip()得到此编号，然后构造html，html是图片的最终直接下载网址。
        string = url.strip('/thumbTags').strip('https://alpha.wallhaven.cc/wallpaper/')
        html = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-' + string + '.jpg'
        pic_path = (self.filePath + keyWord + str(count) + '.jpg' )
        try:
            pic = requests.get(html,headers = self.headers)
            f = open(pic_path,'wb')
            f.write(pic.content)
            f.close()
        except Exception as e:
            print(repr(e))


spider = Spider()
spider.main_fuction()
print('This software will automatically exit in 5 seconds.')
print('本软件将于5秒后自动关闭。')
time.sleep(6)