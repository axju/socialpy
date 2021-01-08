import unittest

from socialpy.storage.generic import BasicStorage


class TestGenericStorage(unittest.TestCase):

    def test_Storage_len(self):
        Storage = BasicStorage()
        self.assertEqual(len(Storage), 0)
        Storage.update('name1')
        self.assertEqual(len(Storage), 1)

    def test_Storage_add(self):
        Storage = BasicStorage()
        self.assertEqual(len(Storage), 0)
        Storage.update('name1')
        self.assertEqual(len(Storage), 1)
        Storage.update('name1', value=5)
        self.assertEqual(len(Storage), 1)
        Storage.update('name1', api='socialpy.apis.dummy', tag='tag', key=1234)
        self.assertEqual(len(Storage), 1)

    def test_Storage_filter(self):
        Storage = BasicStorage()
        Storage.update('name1')
        Storage.update('name2', api='api')
        self.assertEqual(len(list(Storage.filter(api='api'))), 1)
        self.assertEqual(len(list(Storage.filter(api='api1'))), 0)
        self.assertEqual(len(list(Storage.filter(tag='name'))), 0)
        self.assertEqual(len(list(Storage.filter())), 2)

    def test_Storage_getitem(self):
        Storage = BasicStorage()
        Storage['name'] = {'api': 'test'}
        self.assertEqual(len(list(Storage.filter(api='test'))), 1)
        self.assertEqual(len(list(Storage.filter(api='api1'))), 0)


if __name__ == '__main__':
    unittest.main()