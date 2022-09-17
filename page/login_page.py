from selenium.common.exceptions import TimeoutException
from common.browser_engine import browser_engine
from utils.logger import log


class LoginPage(object):

    def __init__(self):
        self.driver = browser_engine

    def get_url(self, url):
        """
                打开网址
                :param url: 网址
                :return:
        """
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(10)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时" % url)

    def refresh(self):
        """
                刷新页面
                :return:
                """
        log.info("刷新页面")
        self.driver.refresh()
        self.driver.implicitly_wait(10)
