# coding:utf-8
'''
Created on 2015年12月26日
抓取网站：http://www.zngirls.com/

抓取过程：
1,根据根URL获取每个人都Index页面URL
2,在Index页面获取个人信息，根据姓名建立文件夹，并保存个人资料
3,根据Index页面生成相册界面(IndexUrl + album/)，获取每个相册的URl
4,在相册页面获取每张图的Url并下载(分页)

注意:
1,此版本暂时直接传入IndexURL，获取指定人的照片
2,每个相册最多获取50张照片(翻页为完善)

@author: Shadow
'''
from spider import UrlManager, HtmlDownloader, Html_Parser, FileManager,\
    EmailUtil
import time
import datetime
import sys

class SpiderMain(object):
    
    # 初始化函数，初始化各模块
    def __init__(self):
        # URL管理器
        self.urlmanager = UrlManager.UrlManager()
        # 下载器
        self.downloader = HtmlDownloader.HtmlDownLoader()
        # 解析器
        self.parser = Html_Parser.HtmlParser()
        # 文件管理器
        self.filemanager = FileManager.FileManager()
        
    
    # 爬取主函数
    # rootUrl 爬取的根Url
    # rootPath 保存根路径
    def crawl(self, rootUrl, rootPath):
        
        # 设置时间格式
        formattime = '%Y-%m-%d %H:%M:%S'
        # 打印开始时间
        beginTime = time.strftime(formattime, time.localtime(time.time()))
        print "开始爬取", beginTime
        
        # 根据根路径获取IndexURL
        # Todo
        
        # 将IndexUrl写入Url管理器
        self.urlmanager.addIndexUrl(rootUrl)
        
        # 相册计数器
        albumCount = 0
        # 相片计数器 
        imageCount = 0
        
        while self.urlmanager.hasIndexUrl():
            
            try:
                ### Index页面操作
                #获取IndexURL
                indexUrl = self.urlmanager.getNewIndexUrl()
                print "获取IndexURL", indexUrl
                
                # 下载IndexURL
                indexDoc = self.downloader.download(indexUrl)
                print "已下载Index页面"
                
                # 解析Index页面，获取个人资料
                name, info = self.parser.parseInfo(indexDoc)
                print "已解析Index页面"
                
                
                # 将个人信息写入文件夹
                # 创建个人相册
                self.filemanager.mkdir(rootPath + "/" + name)
                print "已创建相册", rootPath + "/" + name
                # 创建个人资料文件
                self.filemanager.saveText(info, rootPath + "/" + name, name + ".txt")
                print "已生成个人资料", name + ".txt"
                
                
                
                ### 相册页面操作
                # 生成相册URL
                albumUrl = indexUrl + "album/"
                print "已生成", name, "相册URL", albumUrl
                
                # 下载相册页面
                albumDoc = self.downloader.download(albumUrl)
                print "已下载", name, "的相册页面"
                
                # 解析相册界面，获取每个相册的URL
                albumUrls = self.parser.parseAlbum(albumDoc)
                print "已解析", name, "的相册页面", "获取", len(albumUrls), "个相册"
                
                # 将相册URL写入URL管理器
                self.urlmanager.addAlbumUrls(albumUrls)
                
            
                while self.urlmanager.hasAlbumUrl():
                    
                    try:
                        # 获取未爬取的相册URL
                        albumUrl = self.urlmanager.getNewAlbumUrl()
                        print "已获取相册", albumUrl
                        
                        ### 进入相片页面操作
                        # 下载相片页面
                        imageDoc = self.downloader.download(albumUrl)
                        print "已下载", name, "的相片页面"
                        
                        # 解析相片页面，获取相册标题和所有相片URL,以及包含的其他相片页面(翻页)
                        albumTitle, imageUrls = self.parser.parseImage(imageDoc)
                        print "已解析", name, "的相片页面", "获取", len(imageUrls), "张相片"
                        
                        # 创建相册文件夹
                        self.filemanager.mkdir(rootPath + "/" + name + "/" + albumTitle)
                        print "已创建相册", albumTitle
                        
                        # 将相片URL写入URL管理器
                        self.urlmanager.addImageUrls(imageUrls)
                        
                        ### 相片页面翻页操作
                        # 下载相片页面
                        imageDoc = self.downloader.download(albumUrl)
                        # 解析相片页面包含的其他相片页面(翻页)
                        imagePageUrls = self.parser.parsePageImage(albumUrl, imageDoc)
                        
                        # 将相片页面URL写入URL管理器中
                        self.urlmanager.addImagePageUrls(imagePageUrls)
                        
                        #相册计数
                        albumCount = albumCount + 1
                        
                    except:
                        
                        print "获取相片页面失败", time.strftime(formattime, time.localtime(time.time()))
                        print sys.exc_info()
                    
                    while self.urlmanager.hasImagePageUrl():
                        
                        try:
                            # 获取相片页面
                            imagePageUrl = self.urlmanager.getNewImagePageUrl()
                            print "已获取相片页面", imagePageUrl
                            
                            # 下载相片页面
                            imageDoc = self.downloader.download(imagePageUrl)
                            print "已下载", name, "的相片页面"
                            
                            # 解析相片页面，获取相册标题和所有相片URL,以及包含的其他相片页面(翻页)
                            albumTitle, imageUrls = self.parser.parseImage(imageDoc)
                            print "已解析", name, "的相片页面", "获取", len(imageUrls), "张相片"
                            
                            # 将相片URL写入URL管理器
                            self.urlmanager.addImageUrls(imageUrls)
                        
                        except:
                            print "获取相片其他页面失败", time.strftime(formattime, time.localtime(time.time()))
                            print sys.exc_info()
                    
                    while self.urlmanager.hasImageUrl():
                        
                        try:
                            # 获取相片URL
                            imageUrl = self.urlmanager.getNewImageUrl()
                            print "已获取相片URL", imageUrl
                            
                            imageName = imageUrl.split("/")[-1]
                            # 保存相片
                            self.filemanager.saveImage(imageUrl, rootPath + "/" + name + "/" + albumTitle, imageName)
                            print "已保存相片", imageName
                            
                            imageCount = imageCount + 1
                            
                        except:
                            print "保存相片失败", time.strftime(formattime, time.localtime(time.time()))
                            print sys.exc_info()
                        
            except:
                print "获取相册失败", time.strftime(formattime, time.localtime(time.time()))
                print sys.exc_info()
                
        # 打印结束时间
        endTime = time.strftime(formattime, time.localtime(time.time()))
        print "结束爬取", endTime     
        
        
        # 计算耗时
        beginTime = time.strptime(beginTime, formattime)
        endTime = time.strptime(endTime, formattime)
        time1 = datetime.datetime(beginTime[0],beginTime[1],beginTime[2],beginTime[3],beginTime[4],beginTime[5])
        time2 = datetime.datetime(endTime[0],endTime[1],endTime[2],endTime[3],endTime[4],endTime[5])
        
        cost = time2 - time1
        
        try:
            
            # 向开发者发送邮件
            email = EmailUtil.EmailUtil()
                
            msg = "爬取" + name.encode('utf-8') + "的相册完成"
            msg += "\r\n获取%d个相册" % albumCount
            msg += "\r\n共%d张照片" % imageCount
            msg += "\r\n耗时%s" % cost
                
            print msg
            email.sendEmail("shadowofmind@163.com", "爬取结束", msg)
            
        except:
            print sys.exc_info()
        
        
        
    
    




# 爬虫入口
if __name__ == "__main__":
    # 爬取入口
    rootUrl = "http://www.zngirls.com/girl/19852/"
    # 存储跟路径
    rootPath = "D:/Python/Zngirls"
    spider = SpiderMain()
    spider.crawl(rootUrl, rootPath)
