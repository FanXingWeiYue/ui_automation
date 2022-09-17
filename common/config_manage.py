import os
from utils.time import dt_strftime


class ConfigManager(object):
    # 项目目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 页面元素目录
    ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')
    # 配置文件目录
    CSV_PATH = os.path.join(BASE_DIR, 'data')
    # driver文件
    CHROME_DRIVER = os.path.join(BASE_DIR, 'driver\\chromedriver.exe')
    EDGE_DRIVER = os.path.join(BASE_DIR, 'driver\\msedgedriver.exe')
    # 报告文件
    REPORT_FILE = os.path.join(BASE_DIR, 'report')
    REPORT_NAME = '**测试报告'
    # 截图
    IMG_FILE = os.path.join(BASE_DIR, 'img')

    @property
    def log_file(self):
        """日志目录"""
        log_dir = os.path.join(self.BASE_DIR, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir, '{}.log'.format(dt_strftime()))

    @property
    def ini_file(self):
        """配置文件"""
        ini_file = os.path.join(self.BASE_DIR, 'data', 'url.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在！" % ini_file)
        return ini_file


config_manager = ConfigManager()
if __name__ == '__main__':
    print(config_manager.BASE_DIR)
    print(config_manager.CHROME_DRIVER)
