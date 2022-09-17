from common.browser_engine import browser_engine
from page.elements import Elements


class Search(object):

    def __init__(self):
        self.driver = browser_engine

    def search_fund(self):
        """
                搜索基金
                :param url: 网址
                :return:
        """
        self.driver.find_element(*Elements.search_input).send_keys("110008")
        self.driver.find_element(*Elements.seaCol1).click()