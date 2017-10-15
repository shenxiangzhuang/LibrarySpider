from BookSpider import get_book_data
from MEmail import send_ms

def BooksGo(id, pwd):
    books_info = get_book_data(id, pwd)

    s = ''
    for book_info in books_info:
        s += book_info['title']
        s += '\n'
        s += '借入时间： '
        s += book_info['date_in']
        s += ' 应还时间: '
        s += book_info['date_out']
        s += ' 剩余天数: '
        s += str(book_info['rest_days'])
        s += '\n\n'


    my_email = '1021550072@qq.com'
    send_ms(s, my_email)



if __name__=='__main__':
    BooksGo("学号", "密码")