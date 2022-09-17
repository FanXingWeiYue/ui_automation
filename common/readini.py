import configparser


class ReadIni(object):
    """读取配置文件"""

    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(config_manager.ini_file, encoding='utf-8')

    def get(self, section, option):
        return self.config.get(section, option)

    @property
    def url(self):
        return self.get('HOST', 'host')

    @property
    def username(self):
        return self.get('USERNAME', 'username')

    @property
    def password(self):
        return self.get('PASSWORD', 'password')


ini = ReadIni()

if __name__ == '__main__':
    print(ini.url)
