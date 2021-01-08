from logging import getLogger

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from chromedriver_autoinstaller import install as chromedriver_installer


class BasicSeleniumApi:

    def __init__(self, data_dir):
        super(BasicSeleniumApi, self).__init__()
        self.logger = getLogger('{}.{}'.format(__name__, self.__class__.__name__))

        chromedriver_installer()

        options = Options()
        options.add_argument('user-data-dir={}'.format(data_dir))
        self.browser = Chrome(chrome_options=options)

    def __del__(self):
        try:
            self.browser.quit()
        except Exception as e:
            self.logger.exception('%s', e)
