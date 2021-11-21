from rest_framework.test import APITestCase
from Authentication.models import User


class TestModel(APITestCase):
    def test_creates_user(self):
        user = User.objects.create_user('sushil','susshil@gmail.com','password@')
        self.assertIsInstance(user,User)
        self.assertEqual(user.email,'susshil@gmail.com')
        self.assertFalse(user.is_staff)


    def test_user_when_nouser_is_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username = "", email = 'susshil@gmail.com',password = 'password@')
       

    def test_creates_Superuser(self):
        user = User.objects.create_superuser('sushil','susshil@gmail.com','password@')
        self.assertIsInstance(user,User)
        self.assertEqual(user.email,'susshil@gmail.com')
        self.assertTrue(user.is_staff)