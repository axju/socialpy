from socialpy.storage.misc import FileStorage, EncryptFileStorage


# storage = FileStorage('test.json')
storage = EncryptFileStorage('test.json', '1234')

storage.load()
storage.update('nae', api='socialpy.apis.dummy', tag='tag2', values=5)
for name, item in storage.filter(tag='tag2'):
    print(item)
storage.save()
