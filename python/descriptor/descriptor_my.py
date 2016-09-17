
# 属性的缓存
class _Missing(object):
    def __repr__(self):
        return 'no value'
    
    def __reduce__(self):
        """ pickle 的时候用 确保返回同一个 _missing"""
        return '_missing'

_missing = _Missing()

class cached_property(object):
    def __init__(self,func):
        self.__name__ = func.__name__
        self.__module__ = func.__module__
        self.__doc__ = func.__doc__
        self.func = func

    def __get__(self,obj,owner):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__,_missing)
        if value is _missing:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value

    def __set__(self,instance,value):
        instance.__dict__[self.__name__]=value
        

"""
usage: 存储一些不常改变的属性,比如size=width*height
a=Foo()
a.foo
a.reset_foo()
"""
class Foo(object):
    @cached_property
    def foo(self,name='yaoge'):
        print 'first calculate'
        return 'this is result'
    
    def reset_foo(self):
        self.foo=_missing
