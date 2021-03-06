#coding:utf-8
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(), addr))
def send_ms(text_data, email_addr='xxx@qq.com'):

    from_addr = '1021550072@qq.com'
    password = 'xxx'

    to_addr = email_addr
    smtp_server = 'smtp.qq.com'
    msg = MIMEText(text_data, 'plain', 'utf-8')
    msg['From'] = _format_addr('MySpider')
    msg['To'] = _format_addr('Moonpie')
    msg['Subject'] = Header('The News Report', 'utf-8').encode()
    server = smtplib.SMTP_SSL(smtp_server, 465, timeout=10)
    server.set_debuglevel(0)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


if __name__=='__main__':
    send_ms('test', '1021550072@qq.com')
