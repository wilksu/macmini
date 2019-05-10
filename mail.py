import smtplib
import hrsh
import time
from email.header import Header
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

def kdata():
    s=hrsh.login()
    # t=time.time()
    # t=time.strftime("%Y/%m/%d", time.localtime())
    result=s.get('http://10.64.32.25/KAOQIN/OW/frmOWSearchInfo.aspx?EmpNo=A0245943&OrganNo=GE7260S820&StartDate=2019/04/19&EndDate=2019/04/31&SignStatus=0&OWType=0&OwStatus=0&OwG=0')
    soup = BeautifulSoup(result.text, 'html.parser')
    res=soup.find('table',attrs={'rules':"all"}).find_all('tr')
    a=[]
    for link in res:
        # a=[]
        j=link.find_all('td')
        for i in j:
            if i.find('u') is None:
                # print(i.string)
                a.append(i.string)
            else:
                # print(i.find('u').string)
                a.append(i.find('u').string)
        # print(a[12])
    return a

mail_host = "smtp.yeah.net"      # SMTP服务器
mail_user = "wikisu@yeah.net"                  # 用户名
mail_pass = '134134ww'               # 授权密码，非登录密码

sender = 'wikisu@yeah.net'
receivers = ['wilkki@163.com','wikisu@qq.com']

content = str(kdata())
title = time.strftime("%Y/%m/%d", time.localtime())  # 邮件主题

def sendEmail():

    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()

if __name__ == '__main__':
    # sendEmail()
    print(content)
    