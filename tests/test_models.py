import unittest

from socialpy.models import User


class TestUser(unittest.TestCase):

    def test_userid(self):
        user = User(name='test', ids=[['whatsapp', 'foo']])
        self.assertEqual(user['name'], 'test')
        self.assertIsNone(user.userids('dummy'))
        self.assertEqual(user.userids('whatsapp'), 'foo')
        self.assertEqual(next(user.userids('whatsapp', first=False)), 'foo')


if __name__ == '__main__':
    unittest.main()
