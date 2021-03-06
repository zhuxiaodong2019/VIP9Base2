# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/6 10:50
@Author  : zxd
功能描述：使用python发送邮件
实现步骤：
    1-配置邮箱属性
    2-组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
'''

# 发送html内容的邮件
import smtplib, time
from email.mime.text import MIMEText
from email.header import Header

def sendMail():

    '''发送内容邮件'''
    #第一步：配置邮箱属性

    # 发送邮箱
    sender = 'testing51test@163.com'
    # 接收邮箱
    receiver = 'testing51test@163.com'
    # 发送邮件主题
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    subject = '自动化测试结果_' + t
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户/密码
    username = 'testing51test'
    #注意：如果邮箱从未开启过pop3/smtp服务，则需要进入邮箱设置开启，开启成功后会提示一个授权码，把此处的密码替换为生成的授权码即可
    password = 'AQWYDBASWCLXXJLF'
    # password = 'xxxxxxxx'
    content = 'Python 邮件发送测试...'

    #第二步： 组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    #第三步：登录并发送邮件
    s = None
    try:
        #1--实例化smtp类
        s = smtplib.SMTP()
        #2--连接stmp服务器
        s.connect(smtpserver)
        #3--登录邮箱
        s.login(username, password)
        #4--设置发件人，收件人，邮件内容
        s.sendmail(sender, receiver, msg.as_string())
    except Exception as msg:
        print(u"邮件发送失败！%s"% msg)
    else:
        print("邮件发送成功！")
    finally:
        s.quit()

#调试发送邮件
sendMail()
