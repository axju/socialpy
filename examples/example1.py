from socialpy.client import Gateway

gateway = Gateway()

gateway['instagram'].setup(user='...', pw='...')
#gateway.post(text='auto post...', image='C:/...')
gateway.save_to_file('.env')



#gateway.load_from_file('.env')
#gateway.post(text='New Blog Post #ShortReport #Blog \n https://blog.short-report.de/2018/04/09/easy-bot/')
