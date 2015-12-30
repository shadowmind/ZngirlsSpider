# coding:utf8
'''
Created on 2015年12月25日

@author: Shadow
'''
import os
import urllib2

class FileManager(object):
    
    # 创建指定目录，若存在，则不进行操作
    # path 目录
    def mkdir(self, path):
        if path is None or len(path) == 0:
            return
        
        # 判断路径是否存在
        isExist = os.path.exists(path)
        
        if not isExist:
            os.makedirs(path)
            
    # 保存图片
    # imageUrl 图片URL
    # path 路径
    # filename 文件名
    def saveImage(self, imageUrl, path, filename):
        # 判定是否存在path
        self.mkdir(path)
        # 获取图片数据
        img = urllib2.urlopen(imageUrl, timeout=30)
        # 保存至指定路径
        f = open(path + "/" + filename, "wb")
        f.write(img.read())
        f.close()
        
    # 保存文本
    # content 文本内容
    # path 保存路径
    # filename 文件名
    def saveText(self, content, path, filename):
        # 判定是否存在path
        self.mkdir(path)
        # 保存至指定路径
        f = open(path + "/" + filename, "w+")
        f.write(content.encode("utf-8")) 
        f.close()
        