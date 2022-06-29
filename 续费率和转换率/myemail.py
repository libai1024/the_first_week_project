#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
#设置服务器所需信息
#163邮箱服务器地址
def send_email(receivers,email_body):
    mail_host = 'smtp.qq.com'
    #163用户名
    mail_user = '1422958965'
    #密码(部分邮箱为授权码)
    mail_pass = 'jytmzrzdsrqxgdcc'
    #邮件发送方邮箱地址
    sender = '1422958965@qq.com'
    #邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = receivers

    #设置email信息
    #邮件内容设置

    #接受方信息

    message = MIMEText(email_body, 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = 'title'
    # 发送方信息
    message['From'] = sender
    message['To'] = receivers

    #登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        #连接到服务器
        smtpObj.connect(mail_host,25)
        #登录到服务器
        smtpObj.login(mail_user,mail_pass)
        #发送
        smtpObj.sendmail(
            sender,receivers,message.as_string())
        #退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error',e) #打印错误

