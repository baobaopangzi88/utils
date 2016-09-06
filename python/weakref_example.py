#! /usr/bin/python
# -*- coding:utf8 -*-
import weakref
"""
    这个弱引用据说是在缓存的时候会有用,但是不是很理解，缓存得目的不就是为了保存吗？你通过弱引用释放了,那么要缓存有什么用
    1.然后想到的一个用法是实现单例模式 
"""

class Yao:
    pass 

yao = Yao()
SYao = weakref.ref(yao)

if __name__=="__main__":
    a = SYao()
    b = SYao()
    print a
    print b
    print a==b
