'''

图书馆模拟登录

'''

import requests
import hashlib
import datetime
from bs4 import BeautifulSoup


def get_book_data(studentid, passwd):
    s = requests.session()
    url = 'http://210.37.32.7/opac/reader/doLogin'
    headers = {
        'Connection': 'keep - alive',
        'Cookie': 'JSESSIONID = 9742343A3242C61FC872BE2C7A5DB2CD;org.s'
                  'pringframework.web.servlet.i18n.CookieLocaleResolver.LOCALE = zh',
        'Host': '210.37.32.7',
        'Origin': 'http://210.37.32.7',
        'Referer': 'http://210.37.32.7/opac/reader/login',
        'Upgrade - Insecure - Requests': '1',
        'User - Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, '
                        'like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    # get pwd encode with md5
    hash = hashlib.md5()
    hash.update(str(passwd).encode('utf-8'))
    send_pwd = hash.hexdigest()

    postdata = {
        'rdRegisterName': '',
        'rdid': str(studentid),
        'rdPasswd': send_pwd,
        'returnUrl': '',
        'password': ''
    }

    web_data = s.post(url, headers=headers, data=postdata, verify=False)

    # print(web_data.text)


    # 获取借阅信息
    headers_now = {
        'Connection': 'keep - alive',
        # 'Cookie': 'JSESSIONID=4CA71F348FE0E9557323D9E5C50E5239;'
        #           ' org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh',
        'Host': '210.37.32.7',
        'Referer': 'http://210.37.32.7/opac/reader/login?returnUrl=/loan/currentLoanList',
        'Upgrade - Insecure - Requests': '1',
        'User - Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, '
                        'like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    now_url = 'http://210.37.32.7/opac/loan/currentLoanList'
    now_data = s.get(now_url, headers=headers_now)
    soup = BeautifulSoup(now_data.text, 'lxml')
    books_data = soup.find_all('tr')
    books_info = []
    for i in range(1, len(books_data)):
        book_data = books_data[i]
        book_info = book_data.find_all('td')
        book_info_dict = {}
        book_info_dict['title'] = book_info[1].get_text()
        # 借入时间
        in_date = book_info[6].get_text()
        book_info_dict['date_in'] = in_date
        # 应还时间
        out_date = book_info[7].get_text()
        book_info_dict['date_out'] = out_date
        # 剩余时间[天数]
        book_info_dict['rest_days'] = (datetime.datetime.strptime(out_date, '%Y-%m-%d').date()
                                       - datetime.date.today()).days
        books_info.append(book_info_dict)

    for book_info in books_info:
        print(book_info)
    return books_info


if __name__ == '__main__':
    get_book_data("学号", "密码")
