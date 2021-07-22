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
        cursor.execute('select name,author,')
        books = cursor.fetchone()
    return books

def tokens_left_for_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute('select tokens_left from users where user_id = %s',[user_id])
        tokens = cursor.fetchone()
    return tokens
