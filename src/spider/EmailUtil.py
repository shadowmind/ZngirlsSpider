# coding:utf-8
'''
Created on 2015年12月27日

@author: Shadow
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

# 邮件工具类
class EmailUtil(object):
    
    def __init__(self):
        # 邮件SMTP域名
        self.serverHost = "smtp.163.com"
        # 邮件SMTP端口
        self.serverPort = "25"
        # 用户名
        self.user = "youusername"
        # 密码
        self.password = "youpassword"
        
    # 发送邮件
    # to 目的邮箱
    # subject 邮件标题
    # content 邮件内容
    def sendEmail(self, to, subject, content):
        # 组织邮件信息
        msg = MIMEMultipart()
        msg['From'] = self.user + "@163.com"
        msg['To'] = to
        msg['Subject'] = subject
        # 邮件内容
        text = MIMEText(content)
        msg.attach(text)
        
        try:
            
            ### 发送操作
            smtp = smtplib.SMTP()
            # 连接SMTP服务器
            smtp.connect(self.serverHost, self.serverPort)
            # 登录
            smtp.login(self.user, self.password)
            # 发送邮件
            smtp.sendmail(self.user + "@163.com", to, msg.as_string())
            # 退出smtp服务器
            smtp.quit()
            
            print "已向", to, "发送邮件"
        
        except:
            
            print "向", to, "发送邮件失败"
            print sys.exc_info()
        