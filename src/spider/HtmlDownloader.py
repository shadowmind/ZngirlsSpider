# coding:utf8
'''
Created on 2015年12月21日

@author: Shadow
'''
import urllib2


class HtmlDownLoader(object):
    
    # 下载URL内容
    def download(self, url):
        if url is None:
            return None
        
        try:
            # 使用urllib2下载URL内容
            response = urllib2.urlopen(url, timeout=30)
            
            # 若返回的状态码不是200(成功)，则返回None
            if response.getcode() != 200:
                return None
        except:
            print "下载页面", url, "失败"
        
        return response
    



