# coding:utf8
'''
Created on 2015年12月21日

@author: Shadow
'''
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    
    
    # 解析个人资料
    # indexDoc Index页面Doc

    # 获取姓名
    # soup BeautifulSoup对象
    def getName(self, soup):
        # 格式：<div class="div_h1"><h1 style="font-size: 15px">刘飞儿(Faye)</h1>
        name = soup.find('div', class_='div_h1').find('h1').get_text()
        
        return name
    
    # 获取个人资料
    # soup
    def getInfo(self, soup):
        # 格式：
        # <div class="infodiv"><table><tbody>
        # <tr><td class="info_td">年 龄：</td><td>22 (属鸡)</td></tr>
        # <tr><td class="info_td">生 日：</td><td>1993-03-14</td></tr>
        trs = soup.find('div', class_='infodiv').find_all('tr')
        
        info = ""
        # 遍历获取所有
        for tr in trs:
            tds = tr.find_all('td')
            
            for td in tds:
                info = info + td.get_text()
            info = info + "\n"
        return info    
    
    # 解析个人资料页面
    # indexDoc 需解析的页面
    def parseInfo(self, indexDoc):
        
        # 获取BeautifulSoup对象
        soup = BeautifulSoup(indexDoc, "html.parser", from_encoding="utf-8")
        # 获取女孩名称
        name = self.getName(soup)
        # 获取个人资料
        info = self.getInfo(soup)
        
        return name, info





    # 获取相册URL集合
    # soup
    def getAlbumUrls(self, soup):
        # 格式：<a class='igalleryli_link' href='/g/17545/' >
        links = soup.find_all('a', class_='igalleryli_link')
        
        urls = set()
        for link in links:
            urls.add("http://www.zngirls.com" + link['href'])
        
        return urls
    
    # 解析相册页面
    # albumDoc 需解析的页面
    def parseAlbum(self, albumDoc):
        # 获取BeautifulSoup对象
        soup = BeautifulSoup(albumDoc, "html.parser", from_encoding="utf-8")
        # 获取相册URL集合
        albumUrls = self.getAlbumUrls(soup)
        
        return albumUrls




    
    

    # 解析相册标题
    # soup
    def getAlbumTitle(self, soup):
        # 格式：<h1 id="htilte">刘飞儿Faye-泰国清迈旅拍第一套写真 [秀人网美媛馆]</h1>
        title = soup.find('h1', id='htilte').get_text()
        
        return title
    
    
    # 解析相片URL
    # soup
    def getImageUrls(self, soup):
        # 格式：<ul id="hgallery">
        # <img src='http://img.zngirls.com/gallery/19705/13045/0.jpg' alt='刘飞儿Faye-泰国清迈旅拍第一套写真 [秀人网美媛馆]_0' />
        # <img src='http://img.zngirls.com/gallery/19705/13045/001.jpg' alt='刘飞儿Faye-泰国清迈旅拍第一套写真 [秀人网美媛馆]_1' />
        imgs = soup.find('ul', id='hgallery').find_all('img')
        
        urls = set()
        for img in imgs:
            urls.add(img['src'])
            
        return urls
    
    
    

    
    
    # 解析相片页面
    # imageDoc 需解析的页面
    def parseImage(self, imageDoc):
        # 获取BeautifulSoup对象
        soup = BeautifulSoup(imageDoc, "html.parser", from_encoding="utf-8")
        # 获取相册标题
        albumTitle = self.getAlbumTitle(soup)
        # 获取相片URL集合
        imageUrls = self.getImageUrls(soup)
        
        return albumTitle, imageUrls
    
    
    
    
    # 获取相片页面中其他相片页面URL集合
    # albumUrl 相册URL
    # soup 
    def getImagePageUrls(self, albumUrl, soup):
        # 格式：<div id="pages">
        # <a class='a1' href='/g/13045' >上一页</a><span>1</span>
        # <a href='/g/13045/2.html' >2</a>
        links = soup.find('div', id='pages').find_all('a', href=re.compile(r'.+?\.html'))
        
        urls = set()
        for link in links:
            url = link['href']
            fullUrl = urlparse.urljoin(albumUrl, url)
            urls.add(fullUrl)
            
        return urls
    
    # 解析相片页面包含的其他页面
    # albumUrl 相册URL
    # imageDoc 需解析的页面
    def parsePageImage(self, albumUrl, imageDoc):
        # 获取BeautifulSoup对象
        soup = BeautifulSoup(imageDoc, "html.parser", from_encoding="utf-8")
        # 获取相片页面中其他相片页面URL集合
        imagePageUrls = self.getImagePageUrls(albumUrl, soup)
        
        return imagePageUrls
    
    
    
    
