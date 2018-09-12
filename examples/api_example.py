import logging
import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%d.%m. %H:%M',)



def post(**kwargs):

    params = {}
    if 'text' in kwargs:
        params['text'] = kwargs['text']

    if 'category' in kwargs:
        params['categorys'] = [{'name': kwargs['category']}]

    values = {}
    if 'image' in kwargs:
        values['files'] = {'image': open(kwargs['image'], 'rb')}

    if params:
        values['data'] = params

    print(values)
    headers = {'Content-type': 'application/form-data'}
    return requests.post('http://127.0.0.1:8000/rest/post/', **values)#, headers=headers)



r = post(text='fdgfgdTest', category='news', image='C:/Users/ajura/Pictures/6909249-black-hd-background.jpg')
#r = requests.post('http://127.0.0.1:8000/rest/post/', files={'image': open('C:/Users/ajura/Pictures/6909249-black-hd-background.jpg', 'rb')})
print(r.text)
