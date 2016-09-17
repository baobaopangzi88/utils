# -*- coding:utf8 -*-
"""
    描述符最基础到用法
    
"""



# 静态变量的基本用法
class WebFramework(object):
    def __init__(self,name='Flask'):
        self.name = name

    def __get__(self,instance,owner):
        return self.name
    
    def __set__(self,instance,value):
        print instance,value 
        self.name = value


class PythonSite(object):
    web_framework = WebFramework()

a = PythonSite()
a.web_framework = "aa"





# 常见用法一
from weakref import WeakKeyDictionary
class NonNegative(object):
    def __init__(self,default):
        self.default = default
        # 这个弱引用很关键否则不会被释放
        self.data = WeakKeyDictionary()

    def __get__(self,instance,owner):
        print 'this is get'
        return self.data.get(instance, self.default)

    def __set__(self,instance,value):
        print 'this is set '
        if value<0:
            raise ValueError('Negative value')
        self.data[instance]=value

class Movie(object):
    budget = NonNegative(0)

    def __init__(self,budget=0):
        self.data=[None]*10**8
    



# unhashable类中描述器用法
class Descriptor(object):
    def __init__(self,label):
        self.label = label
        self.data = {}

    def __get__(self,instance,owner):
        return instance.__dict__.get(self.label)

    def __set__(self,instance,value):
        self.data[self.label] = value
        instance.__dict__[self.label] = value


class FooList(list):
    x = Descriptor('x')
    y = Descriptor('y')






# 重载元类自动赋值label的用法
class Descriptor(object):
    def __init__(self):
        """ 是在元类中赋值的 """
        self.label = None

    def __get__(self,instance,owner):
        return instance.__dict__.get(self.label)

    def __set__(self,instance,value):
        instance.__dict__[self.label]=value


class DescriptorOwner(type):
    def __new__(cls,name,bases,attrs):
        print cls
        print name
        print bases
        print attrs
        for n,v in attrs.items():
            if isinstance(v,Descriptor):
                v.label = n
                print n,type(n)
        return super(DescriptorOwner,cls).__new__(cls,name,bases,attrs)


class Foo(object):
    __metaclass__ = DescriptorOwner
    x = Descriptor()




    

# 自定义回调函数的用法
class CallbackProperty(object):
    """A property that will alert observers when upon updates"""
    def __init__(self, default=None):
        self.data = WeakKeyDictionary()
        self.default = default
        self.callbacks = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance==None:
            print self
            return self
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):        
        for callback in self.callbacks.get(instance, []):
            # alert callback function of new value
            callback(value)
        self.data[instance] = value

    def add_callback(self, instance, callback):
        """Add a new function to call everytime the descriptor updates"""
        #but how do we get here?!?!
        if instance not in self.callbacks:
            self.callbacks[instance] = []
        self.callbacks[instance].append(callback)
 

class BankAccount(object):
    balance = CallbackProperty(0)

def low_balance_warning(value):
    if value < 100:
        print "You are poor"

ba = BankAccount()
BankAccount.balance.add_callback(ba, low_balance_warning)





