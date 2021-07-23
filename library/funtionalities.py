from typing import Counter
from django.db import connection
from library import models


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
                if res == None:
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
