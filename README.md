# utils  
对一些经常使用的代码写了详细的文档，方便查阅。  
  
### /python/tools  
  
- **genpass** 一个生成密码的小工具  
 适用于安全性较高的场合  
  
### /python/decorator  
- **decorator_basic.py** 装饰器的基本用法  
    - 带参数装饰器的用法  
    - 装饰器嵌套装饰器的顺序  
    - 用类实现装饰器  
    - 用函数实现装饰器  
  
  
- **decorator_official.py** 官方的常用装饰器  
    - 保存使用装饰器前的原函数名字、注释等属性(装饰器的装饰器)  
    - 缓存含有ttl值的属性  
        比如每隔1个小时会变动的access_token,可以用这个装饰器缓存  
    - 基本属性的实现  
        包含获取，设置，删除  
    - 缓存不同参数的函数的值(不含ttl)  
  
  
- **decorator_my.py** 自己整理的装饰器用法  
    - web应用中返回给前端json数据  
    - 缓存不同参数的函数的值(含ttl)  
    - 互斥锁  
    - 单例模式  
    - 多线程计算  
  
  
### /python  
  
  
  
- **weakref_basic.py** 弱引用的基本用法  
- **weakref_example.py** 弱引用的用法实例  
  
  
### /python/descriptor  
- **descriptor_basic.py** 描述器的基本用法  
    - 静态变量的基本用法  
    - 常见用法  
    - unhashable类中描述器用法  
    - 重载元类自动赋值label的用法  
    - 自定义回调函数的用法  
  
- **descriptor_official.py** 官方描述器的一些用法  
    - 设置属性用法  
  
- **descriptor_my.py** 自己整理的描述器的用法  
    - 属性的缓存  
  
### /linux  
* **rm_redirect** 修改rm命令  
   因为rm和mv很相似,修改后可以避免很多麻烦。如果确实要删除，可以用/bin/rm  
* **virtual_memory** 增加虚拟内存  
   多用于极耗内存的一次性的运算。  
  
  
