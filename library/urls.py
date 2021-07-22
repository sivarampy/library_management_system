from django.urls import path
from . import views


urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('login/',views.login,name='login_page'),
    path('registration/',views.registration,name='registration_page'),
    path('HomePage/',views.user,name='user_home_page'),
    path('SearchBook/',views.search_book,name='user_search_book'),
    path('BorrowedBooks/',views.borrowed_books,name='borrowed_books'),
    path('librarian/',views.user_librarian,name='user_libraian_page'),
]