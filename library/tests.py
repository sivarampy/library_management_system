from django.test import TestCase
import os
from . import models



class test_database_connection(TestCase):

    def test_users_table(self):
        models.Users.objects.create(user_name='sivaram',email='sivaram@gmail.com',password='sivaram',user_type='student',tokens_left=5,phone='9182363820')
        user = models.Users.objects.filter(user_name='sivaram')
        assert (user[0].email == 'sivaram@gmail.com')
        

