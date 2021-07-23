from django.shortcuts import redirect, render
from . import funtionalities

# Create your views here.
def home_page(request):
    return render(request,'home_page.html')

def login(request):
    if request.session.get('logged_in',False) == False:
        if request.method == 'POST':
            res = funtionalities.login_functionality(request.POST['email'],request.POST['pwd'])
            if res == 'login failed':
                return redirect('/login/')
            else:
                request.session['user_id'] = res[0]
                request.session['logged_in'] = True
                request.session['user_type'] = res[1]
                if res[1] == 'student':
                    return redirect('/HomePage/')
                else:
                    return redirect('/AdminPage/')
        else:
            return render(request,'login_page.html')
    else:
        if request.session.get('user_type') == 'student':
            return redirect('/HomePage/')
        else:
            return redirect('/AdminPage/')

def registration(request):
    if request.session.get('logged_in',False) == False:
        if request.method == 'POST':
            name = request.POST.get('name')
            pwd = request.POST.get('pwd')
            conf_pwd = request.POST.get('conf_pwd')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            res = funtionalities.registration_functionality(name,pwd,conf_pwd,email,phone)
            if res == 'password not matched':
                return redirect('/registration/')
            elif res == 'user already exits':
                return redirect('/registration/')
            elif res == 'did not entered details':
                return redirect('/registration/')
            else:
                return redirect('/login/')
        else:
            return render(request,'registration_page.html')
    else:
        if request.session.get('user_type') == 'student':
            return redirect('/HomePage/')
        else:
            return redirect('/AdminPage/')

def logout(request):
    if request.method == 'POST':
        request.session.flush()
    return redirect('/login/')


def user_home_page(request):
    if request.session.get('logged_in',False) == True:
        user_id = request.session.get('user_id')
        tokens = funtionalities.tokens_left_for_user(user_id)
        texts = funtionalities.messages_for_user(user_id)
        return render(request,'user_home_page.html',{'tokens':tokens,'texts':texts})
    else:
        return redirect('/login/')

def search_book(request):
    if request.session.get('logged_in',False) == True:
        user_id = request.session.get('user_id')
        tokens = funtionalities.tokens_left_for_user(user_id)[0]
        if request.method == 'POST':
            entered_key = request.POST.get('search')
            request.session['entered_key'] = entered_key
            books = funtionalities.search_book_for_user(entered_key)
            return render(request,'user_search_books_page.html',{'books':books,'tokens':tokens})
        elif request.session.get('entered_key',None):
            entered_key = request.session.get('entered_key')
            books = funtionalities.search_book_for_user(entered_key)
            return render(request,'user_search_books_page.html',{'books':books,'tokens':tokens})
        else:
            return render(request,'user_search_books_page.html')
    else:
        return redirect('/login/')

def borrowed_books(request):
    if request.session.get('logged_in',False) == True:
        user_id = request.session.get('user_id')
        books = funtionalities.borrowed_books_by_user(user_id)
        return render(request,'user_borrowed_books_page.html',{'books':books})
    else:
        return redirect('/login/')

def borrow(request):
    if request.session.get('logged_in',False) == True:
        user_id = request.session.get('user_id')
        if request.method == 'POST':
            book_id = request.POST.get('borrow')
            funtionalities.borrow_book_for_user(book_id,user_id)
        return redirect('/SearchBook/')
    else:
        return redirect('/login/')

def user_librarian(request):
    if request.session.get('logged_in',False) == True:
        user_id = request.session.get('user_id')
        details = funtionalities.librarian_details()
        if request.method == 'POST':
            text = request.POST.get('message')
            funtionalities.send_message_to_admin(user_id,text)
            sent = 1
            return render(request,'user_librarian_page.html',{'sent':sent})
        sent = 0
        return render(request,'user_librarian_page.html',{'details':details,'sent':sent})
    else:
        return redirect('/login/')
    