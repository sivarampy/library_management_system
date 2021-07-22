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

def user(request):
    return render(request,'user_home_page.html')

def search_book(request):
    return render(request,'search_books.html')

def borrowed_books(request):
    return render(request,'borrowed_books.html')

def user_librarian(request):
    return render(request,'user_librarian_page.html')