from unittest import TestCase
from models.user import UserModel


class TestUser(TestCase):
    def test_create_user(self):
        user = UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test',
                         "The name of the user after creation does not equal the constructor argument.")
        self.assertEqual(user.password, 'abcd',
                         "The password of the user after creation does not equal the constructor argument.")
