import os
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from socialpy.apis.selenium import BasicSeleniumApi
from socialpy.commands.generic import BasicConfig
from socialpy.utils import manage_filenames


class WhatsAppApi(BasicSeleniumApi):
    """docstring for WhatsAppApi."""

    def __init__(self, data_dir):
        super(WhatsAppApi, self).__init__(data_dir)
        self.browser.get('https://web.whatsapp.com')

    def check_login(self, timeout=20):
        """return true if you ar login"""
        for i in range(timeout):
            try:
                self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/header/div[1]/div/img')
                return True
            except NoSuchElementException:
                sleep(1)
            except Exception as e:
                raise e
        return False

    def login(self):
        while not self.check_login():
            self.logger.info('scan the QR code!')
        self.logger.info('Now you are loged in')

    def friends(self, **kwargs):
        if not self.check_login():
            return []
        return []

    def chats(self, **kwargs):
        if not self.check_login():
            return []
        elm = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/header/div[1]/div/img')
        print(elm)
        return []


class WhatsAppConfig(BasicConfig):

    values = {
        'data_dir': {
            'short': 'd',
            'help': 'data_dir',
            'type': str,
            'default': manage_filenames('selenium')
        }
    }

    def handle(self, args):
        kwargs = super(WhatsAppConfig, self).handle(args)
        kwargs['data_dir'] = os.path.abspath(kwargs['data_dir'])
        api = WhatsAppApi(**kwargs)
        api.login()
        return kwargs
