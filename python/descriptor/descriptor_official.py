



# 设置属性用法
class Movie(object):
    def __init__(self,budget=None):
        self._budget = None

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self,value):
        if value<0:
            raise ValueError('Negative value')
        self._budget = value

    @property
    def total_budget(self):
        return self.budget * 2

