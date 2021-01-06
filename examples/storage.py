from socialpy.storage.generic import FileStorage


storage = FileStorage('test.json')

storage.load()
storage.update('nae', api='socialpy.apis.dummy', tag='tag2', values=5)
for name, item in storage.filter(tag='tag'):
    print(item)
storage.save()
