from django.db import models

# Create your models here.
class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=121, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=34, blank=True, null=True)  # Field name made lowercase.
    user_rating = models.DecimalField(db_column='User Rating', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reviews = models.IntegerField(db_column='Reviews', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'books'

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=75)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=25)
    user_type = models.CharField(max_length=10)
    tokens_left = models.IntegerField()
    phone = models.CharField(max_length=10,default='NA')

    class Meta:
        db_table = 'users'


class BorrowedBooksData(models.Model):
    book = models.ForeignKey(Books,on_delete= models.DO_NOTHING)
    user = models.ForeignKey(Users,on_delete= models.DO_NOTHING)
    date_borrowed = models.DateField()

    class Meta:
        db_table = 'borrowed_books_data'

class Location(models.Model):
    book= models.ForeignKey(Books,on_delete= models.DO_NOTHING)
    floor = models.IntegerField()
    rack = models.IntegerField()

    class Meta:
        db_table = 'location'


