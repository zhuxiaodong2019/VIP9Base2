# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/6 11:24
@Author  : zxd
@功能: 发送带有附件的邮件
'''

# 发送html附件的邮件
import smtplib, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def send_mail_html():
    '''发送html附件'''
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
    password = 'AQWYDBASWCLXXJLF'
    file = 'test.html'
    # 读取html文件内容   with open自带close功能
    with open(file,'rb') as f:
        mail_body = f.read()

        # 组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
        msg = MIMEMultipart()  #多个
        #添加附件
        att = MIMEText(mail_body, 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=report1.html'
        msg.attach(att)
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = sender
        msg['To'] = receiver

    #第三步：登录并发送邮件
    smtp = None
    try:
        #1--实例化smtp类
        smtp = smtplib.SMTP()
        #2--连接stmp服务器
        smtp.connect(smtpserver)
        #3--登录邮箱
        smtp.login(username, password)
        #4--设置发件人，收件人，邮件内容
        smtp.sendmail(sender, receiver, msg.as_string())
    except:
        print("邮件发送失败！")
    else:
        print("邮件发送成功！")
    finally:
        smtp.quit()


if __name__ == '__main__':

    send_mail_html()