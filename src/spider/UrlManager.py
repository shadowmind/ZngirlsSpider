# coding:utf-8
'''
Created on 2015年12月26日

@author: Shadow
URL管理类

'''

# URL管理类
class UrlManager(object):
    
    # 初始化各URL集合
    def __init__(self):
        # IndexURL集合
        self.unCrawlIndexUrls = set()
        self.crawledIndexUrls = set()
        # 相册URL集合
        self.unCrawlAlbumUrls = set()
        self.crawledAlbumUrls = set()
        # 相片URL结合
        self.unCrawlImageUrls = set()
        self.crawledImageUrls = set()
        # 相片翻页URL集合
        self.unCrawlImagePageUrls = set()
        self.crawledImagePageUrls = set()
        
        
    # --------------------------   处理IndexUrl Begin   --------------------------------------------
    # 增加IndexUrl
    def addIndexUrl(self, indexUrl):
        if indexUrl is None:
            return
        
        if indexUrl not in self.unCrawlIndexUrls and indexUrl not in self.crawledIndexUrls:
            self.unCrawlIndexUrls.add(indexUrl)
    
    # 批量增加IndexURL
    def addIndexUrls(self, indexUrls):
        if indexUrls is None or len(indexUrls) == 0:
            return
        
        for indexUrl in indexUrls:
            self.addIndexUrl(indexUrl)

    
    # 检测为爬取的IndexURL集合中是否存在URL
    def hasIndexUrl(self):
        return len(self.unCrawlIndexUrls) != 0


    # 获取一个未爬取的IndexURL
    def getNewIndexUrl(self):
        url = self.unCrawlIndexUrls.pop()
        self.crawledIndexUrls.add(url)
        
        return url
    
    # --------------------------   处理IndexUrl End   --------------------------------------------
    
    
    # --------------------------   处理AlbumUrl Begin   --------------------------------------------
    # 增加AlbumUrl
    def addAlbumUrl(self, albumUrl):
        if albumUrl is None:
            return
        
        if albumUrl not in self.unCrawlAlbumUrls and albumUrl not in self.crawledAlbumUrls:
            self.unCrawlAlbumUrls.add(albumUrl)
    
    # 批量增加AlbumUrl
    def addAlbumUrls(self, albumUrls):
        if albumUrls is None or len(albumUrls) == 0:
            return
        
        for albumUrl in albumUrls:
            self.addAlbumUrl(albumUrl)

    
    # 检测为爬取的AlbumUrl集合中是否存在URL
    def hasAlbumUrl(self):
        return len(self.unCrawlAlbumUrls) != 0


    # 获取一个未爬取的AlbumUrl
    def getNewAlbumUrl(self):
        url = self.unCrawlAlbumUrls.pop()
        self.crawledAlbumUrls.add(url)
        
        return url
    
    # --------------------------   处理AlbumUrl End   --------------------------------------------
    
    
    
    # --------------------------   处理ImageUrl Begin   --------------------------------------------
    # 增加ImageUrl
    def addImageUrl(self, imageUrl):
        if imageUrl is None:
            return
        
        if imageUrl not in self.unCrawlImageUrls and imageUrl not in self.crawledImageUrls:
            self.unCrawlImageUrls.add(imageUrl)
    
    # 批量增加ImageURL
    def addImageUrls(self, imageUrls):
        if imageUrls is None or len(imageUrls) == 0:
            return
        
        for imageUrl in imageUrls:
            self.addImageUrl(imageUrl)

    
    # 检测为爬取的ImageURL集合中是否存在URL
    def hasImageUrl(self):
        return len(self.unCrawlImageUrls) != 0


    # 获取一个未爬取的ImageURL
    def getNewImageUrl(self):
        url = self.unCrawlImageUrls.pop()
        self.crawledImageUrls.add(url)
        
        return url
    
    # --------------------------   处理ImageUrl End   --------------------------------------------
    
    
    
    # --------------------------   处理ImagePageUrl Begin   --------------------------------------------
    # 增加ImagePageUrl
    def addImagePageUrl(self, imagePageUrl):
        if imagePageUrl is None:
            return
        
        if imagePageUrl not in self.unCrawlImagePageUrls and imagePageUrl not in self.crawledImagePageUrls:
            self.unCrawlImagePageUrls.add(imagePageUrl)
    
    # 批量增加ImagePageURL
    def addImagePageUrls(self, imagePageUrls):
        if imagePageUrls is None or len(imagePageUrls) == 0:
            return
        
        for imagePageUrl in imagePageUrls:
            self.addImagePageUrl(imagePageUrl)

    
    # 检测为爬取的ImagePageURL集合中是否存在URL
    def hasImagePageUrl(self):
        return len(self.unCrawlImagePageUrls) != 0


    # 获取一个未爬取的ImageURL
    def getNewImagePageUrl(self):
        url = self.unCrawlImagePageUrls.pop()
        self.crawledImagePageUrls.add(url)
        
        return url
    
    # --------------------------   处理ImagePageUrl End   --------------------------------------------
    
    
    
    
    
    



