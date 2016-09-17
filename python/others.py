# classmethod 和 staticmethod 的区别
class PythonSite(object):
    """ classmethod 和 staticmethod 几乎一样只是一个需要硬编码"""
    version = 0.1

    @classmethod
    def get_version(cls):
        return cls.version
    
    @staticmethod
    def find_version():
        return PythonSite.version

