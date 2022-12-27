from unittest import TestCase
from models.store import StoreModel


class TestStore(TestCase):
    def test_create_store(self):
        store = StoreModel('test')

        self.assertEqual(store.name, 'test', "The name of the store does not equal the constructor argument.")
