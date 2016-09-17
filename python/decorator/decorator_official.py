# -*- coding:utf8 -*-


# 保存使用装饰器前的原函数名字、注释等属性(装饰器的装饰器)
def simple_decorator(decorator):
    def new_decorator(f):
        g = decorator(f)
        g.__name__ = f.__name__
        g.__doc__ = f.__doc__
        g.__dict__.update(f.__dict__)
        return g
    new_decorator.__name__ = decorator.__name__
    new_decorator.__doc__ = decorator.__doc__
    new_decorator.__dict__.update(decorator.__dict__)
    return new_decorator

# Sample Usage:
@simple_decorator
def my_simple_logging_decorator(func):
    def you_will_never_see_this_name(*args, **kwargs):
        print 'calling {}'.format(func.__name__)
        return func(*args, **kwargs)
    return you_will_never_see_this_name

@my_simple_logging_decorator
def double(x):
    'Doubles a number.'
    return 2 * x










# 缓存类中属性,包含ttl值(比如每隔1个小时会变动的access_token,可以用这个装饰器缓存)
class cached_property(object):
    def __init__(self, ttl=300):
        self.ttl = ttl

    def __call__(self, fget):
        self.fget = fget
        self.__doc__ = fget.__doc__
        self.__name__ = fget.__name__
        self.__module__ = fget.__module__
        return self

    def __get__(self, inst, owner):
        now = time.time()
        try:
            value, last_update = inst._cache[self.__name__]
            if self.ttl > 0 and now - last_update > self.ttl:
                raise AttributeError
        except (KeyError, AttributeError):
            value = self.fget(inst)
            try:
                cache = inst._cache
            except AttributeError:
                cache = inst._cache = {}
            cache[self.__name__] = (value, now)
        return value


# Sample Usage:
class myclass(object):
    # create property whose value is cached for ten minutes
    @cached_property(ttl=600)
    def randint(self):
        """ will only be evaluated every 10 min. at maximum. """
        return random.randint(0, 100)








# 基本属性的实现
# 包含获取，设置，删除
class A(object):
    @property
    def rad():
        '''The angle in radians'''
        def fget(self):
            return self._rad

        def fset(self, angle):
            if isinstance(angle, Angle):
                angle = angle.rad
            self._rad = float(angle)

        def fdel(self):
            del self._half









# 缓存不同参数的函数的值
import collections
import functools
class memoized(object):
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         print "__call__",args
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      ''' 为了在类中也可以使用  '''
      return functools.partial(self.__call__, obj)


@memoized
def fibonacci(n):
   "Return the nth fibonacci number."
   if n in (0, 1):
      return n
   return fibonacci(n-1) + fibonacci(n-2)



if __name__=="__main__":
    # assert double.__name__ == 'double'
    # assert double.__doc__ == 'Doubles a number.'
    fibonacci(8)



