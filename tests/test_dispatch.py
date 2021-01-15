import unittest

from socialpy.dispatch import ApiDispatcher


class TestApiDispatcher(unittest.TestCase):

    def test_Storage_len(self):
        api = ApiDispatcher('socialpy.dummy', kwargs={'username': 'test', 'password': 'test'})
        self.assertEqual('login', api.login())


if __name__ == '__main__':
    unittest.main()
