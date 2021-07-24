from django.db import connection


def login_functionality(email,pwd):
    with connection.cursor() as cursor:
        cursor.execute('select user_id,user_type from users where email = %s and password = %s',[email,pwd])
        res = cursor.fetchone()
    if res:
        return res
    else:
        return 'login failed'

def registration_functionality(name,pwd,conf_pwd,email,phone):
    if name == '' or pwd == '' or conf_pwd == '' or email == '' or phone == '':
        return 'did not entered details'
    else:
        if pwd == conf_pwd:
            with connection.cursor() as cursor:
                cursor.execute('select user_type from users where email = %s',[email])
                res = cursor.fetchone()
                cursor.execute('select user_type from users where user_name = %s',[name])
                rus = cursor.fetchone()
                if res == None and rus == None:
                    cursor.execute('insert into users (user_name,email,password,phone) values (%s,%s,%s,%s)',[name,email,pwd,phone])
                else:
                    return 'user already exits'
        else:
            return 'password not matched'

def borrowed_books_by_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute('select name,author,price,date_borrowed from books join borrowed_books_data on books.book_id = borrowed_books_data.book_id where borrowed_books_data.user_id = %s',[user_id])
        books = cursor.fetchall()
    return books

def messages_for_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute('select message,from_ads,date_sent from messages where to_ads = %s',[user_id])
        texts = cursor.fetchall()
    return texts

def tokens_left_for_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute('select tokens_left from users where user_id = %s',[user_id])
        tokens = cursor.fetchone()
    return tokens

def search_book_for_user(entered_key):
    if entered_key:
        with connection.cursor() as cursor:
            cursor.execute('select name,author,price,floor,rack,book_status,books.book_id from books join location on books.book_id = location.book_id where name like %s',['%'+entered_key+'%'])
            books = cursor.fetchall()
        return books
    else:
        return None

def borrow_book_for_user(book_id,user_id):
    with connection.cursor() as cursor:
        cursor.execute('update books set book_status = "borrowed" where book_id = %s',[book_id])
        cursor.execute('insert into borrowed_books_data values (%s,%s,sysdate())',[book_id,user_id])
        cursor.execute('select tokens_left from users where user_id = %s',[user_id])
        tokens = cursor.fetchone()
        cursor.execute('update users set tokens_left = %s where user_id = %s',[tokens[0]-1,user_id])
    return 

def librarian_details():
    with connection.cursor() as cursor:
        cursor.execute('select * from users where user_type = "librarian"')
        details = cursor.fetchone()
    return details

def send_message_to_admin(user_id,text):
    with connection.cursor() as cursor:
        cursor.execute('select user_name from users where user_id = %s',[user_id])
        from_ads = cursor.fetchone()
        cursor.execute('select user_id from users where user_type = "librarian"')
        admin = cursor.fetchone()
        cursor.execute('select max(message_id) from messages')
        m_id = cursor.fetchone()
        if not m_id[0]:
            m_id = (0,)
        cursor.execute('insert into messages (message_id,message,from_ads,to_ads,date_sent) values (%s,%s,%s,%s,sysdate())',[m_id[0]+1,text,from_ads[0],admin[0]])
    return
