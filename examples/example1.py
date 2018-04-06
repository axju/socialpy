from socialpy import Gateway

gateway = Gateway()

#gateway.load_from_file('.env')

gateway['twitter'].load({
    'ckey': '1234',
    #'csecret': '123',
    #'akey': '123',
    'asecret': '123',
})

#gateway['facebook'].login('1234', '1234')
gateway['instagram'].login('1234', '1234')
gateway.post(text='bla bla bla')

gateway.save_to_file('.env')
