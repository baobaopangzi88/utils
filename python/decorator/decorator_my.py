
# web应用中返回给前端json数据
ALLOWED_ORIGINS_PAT = re.compile(r"https?://(\w+\.)?(wantjr)\.(com|cn|cc)")
def json_decorator(func):
    """ 
        web应用中，常常会需要返回json数据给前端调用。
        为了前后端交互更方便,可以简单的把域名的前缀替换即可

        样例:
        @json_decorator
        def my_view(request,a,b,c,template="home.html"):
            context = {"name":"bob"}
            return context

        访问 json.wantjr.com 返回数据
        访问 www.wantjr.com 返回正常网页

    """
    def _deco(request,*args, **kwargs):
        # 正式context
        context = func(request, *args, **kwargs)
        # 判断是否请求数据
        if request.get_host()[:4] == "json":
            response =  HttpResponse(json.dumps(context), content_type="application/json")
            origin_addr = request.META.get("HTTP_ORIGIN", "")
            # 处理跨域请求
            if ALLOWED_ORIGINS_PAT.match(origin_addr):
                response['Access-Control-Allow-Origin'] = origin_addr
        # 后端可能有重定向的需求
        elif context.get("redirect_url"):
            response = HttpResponseRedirect(context.get("redirect_url"))
        else:
            template = kwargs.get("template","home.html")
            # 可能有返回不同模板的需求
            if context.get("template"):
                template = context.get("template")
            response = render(request,template,context)

        return response
    return _deco
return json_decorator








#  缓存不同参数的函数的值(含ttl)
class cached_func(object):
    """ 
        用来缓存类中方法的装饰器
            局限性是只能用在类中的方法,好处是可扩展性强
        根据ttl值和传入得参数不同来判断是否从缓存还是实时获取
    """
    def __init__(self, ttl=300):
        self.cache = {}
        self.timestamp = {}
        self.ttl = ttl

    def __call__(self, func):
        self.func = func
        return self

    def get_result(self, *args ,**kwargs):
        key = str(args)+str(kwargs)
        if key not in self.cache or self.timestamp[key] + self.ttl < time.time():
            self.cache[key] = self.func(*args,**kwargs)
            self.timestamp[key] = time.time() 
        return self.cache[key]

    def __get__(self,obj,objtype):
        return functools.partial(self.get_result, obj)

# example
class MyClass(object):
    @cached_func(ttl=6)
    def get_data(self, n=0):
        time.sleep(3)
        return n
        

def cached_func2(ttl):
    """ 
        用来缓存方法的装饰器
            局限性是可读性较差,好处是类和方法中都能使用
        根据ttl值和传入得参数不同来判断是否从缓存还是实时获取
    """
    cache = {}
    timestamp = {}
    def _deco(func):
        def __deco(*args,**kwargs):
            key = str(args) + str(kwargs)
            if key not in cache or timestamp[key] + ttl<time.time():
                cache[key] = func(*args,**kwargs)
                timestamp[key] = time.time() 
            return cache[key]
        return __deco
    return _deco

# example
class MyClass(object):
    @cached_func2(ttl=6)
    def get_data(self, n=0):
        time.sleep(3)
        return n

@cached_func2(ttl=6)
def get_data(n=0):
    time.sleep(3)
    return n





# 互斥锁
from threading import Lock
my_lock = Lock()

def synchronized(lock):
    def wrap(func):
        def _wrap(*args,**kwargs):
            lock.acquire()
            try:
                return func(*args,**kwargs)
            finally:
                lock.release()
        return _wrap
    return wrap

@synchronized(my_lock)
def show():
    time.sleep(1)
    print "hao"



# 单例模式
import functools
def singleton(cls):
    ''' Use class as singleton. '''
    cls.__new_original__ = cls.__new__
    @functools.wraps(cls.__new__)
    def singleton_new(cls, *args, **kw):
        it =  cls.__dict__.get('__it__')
        if it is not None:
            return it

        cls.__it__ = it = cls.__new_original__(cls, *args, **kw)
        it.__init_original__(*args, **kw)
        return it
    cls.__new__ = singleton_new
    cls.__init_original__ = cls.__init__
    cls.__init__ = object.__init__
    return cls


# 多线程计算
import threading, sys, functools, traceback
def lazy_thunkify(f):
    """Make a function immediately return a function of no args which, when called,
    waits for the result, which will start being processed in another thread.

    sample usage:
        @lazy_thunkify
        def slow_double(i):
            print "slow_double start"
            time.sleep(5)
            print "slow_double end"
            return i*2

        res  = show_double(1)
        return res()
    """

    @functools.wraps(f)
    def lazy_thunked(*args, **kwargs):
        wait_event = threading.Event()
        result = [None]
        exc = [False, None]
        def worker_func():
            try:
                func_result = f(*args, **kwargs)
                result[0] = func_result
            except Exception, e:
                exc[0] = True
                exc[1] = sys.exc_info()
                print "Lazy thunk has thrown an exception (will be raised on thunk()):\n%s" % (
                    traceback.format_exc())
            finally:
                wait_event.set()

        def thunk():
            wait_event.wait()
            if exc[0]:
                raise exc[1][0], exc[1][1], exc[1][2]

            return result[0]
        threading.Thread(target=worker_func).start()
        return thunk
    return lazy_thunked





