from django.test import TestCase
from . import models



class test_database_connection(TestCase):

    def test_users_table(self):
        models.Users.objects.create(user_name='sivaram',email='sivaram@gmail.com',password='sivaram',user_type='student',tokens_left=5,phone='9182363820')
        models.Users.objects.create(user_name='rohit',email='rohit@gmail.com',password='rohit',user_type='student',tokens_left=5,phone='9502046478')
        user = models.Users.objects.filter(user_name='sivaram')
        assert (user[0].email == 'sivaram@gmail.com')

    def test_message_table(self):
        models.Users.objects.create(user_id=1,user_name='sivaram',email='sivaram@gmail.com',password='sivaram',user_type='student',tokens_left=5,phone='9182363820')
        models.Users.objects.create(user_id=2,user_name='rohit',email='rohit@gmail.com',password='rohit',user_type='student',tokens_left=5,phone='9502046478')
        models.Messages.objects.create(message_id=1,message='hello rohit',from_ads=models.Users.objects.get(user_id=1),to_ads=models.Users.objects.get(user_id=2),date_sent='2021-07-21')
        message = models.Messages.objects.filter(message_id=1)
        assert (message[0].message == 'hello rohit')
        

