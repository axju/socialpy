import os
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from socialpy.apis.selenium import BasicSeleniumApi
from socialpy.commands.generic import BasicConfig
from socialpy.utils import manage_filenames


class WhatsAppApi(BasicSeleniumApi):
    """docstring for WhatsAppApi."""

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
        self.browser.get('https://web.whatsapp.com')
        while not self.check_login():
            self.logger.info('Please wait or scan the QR code!')
        self.logger.info('Now you are loged in')

    def friends(self, **kwargs):
        if not self.check_login():
            return []
        return []

    def chats(self):
        if not self.check_login():
            return []
        elms = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div')
        for elm in elms.find_elements_by_xpath('div'):
            name = elm.find_element_by_xpath('div/div/div[2]/div[1]/div[1]').text
            status = elm.find_element_by_xpath('div/div/div[2]/div[2]').text
            yield {'id': name, 'status': status}

    def send(self, message, user=None, chat=None):
        id = user.get('ids', {}).get('socialpy.whatsapp')
        elm = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
        elm.send_keys(id)
        sleep(1)
        elm.send_keys(Keys.ENTER)
        sleep(1)
        elm = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
        elm.send_keys(message + Keys.ENTER)


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
