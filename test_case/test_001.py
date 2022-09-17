from page.login_page import LoginPage
from page.search import Search

login_page = LoginPage()
search = Search()
if __name__ == '__main__':
    login_page.get_url("https://fund.eastmoney.com/")
    search.search_fund()
