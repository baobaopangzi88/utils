#! /usr/bin/python
import weakref
import gc
import time


class Yao:
    pass

def call_back(reference,label=""):
    print "I am callback %s\n"%reference

def run():
    gc.disable()
    gc.set_debug(gc.DEBUG_LEAK)

    weak_value_dict = weakref.WeakValueDictionary()    
    weak_value_dict[1]=Yao()
    # print weak_value_dict.items()

    weak_key_dict = weakref.WeakKeyDictionary()
    weak_key_dict[Yao()]=1
    # print weak_key_dict.items()
    
    yao = Yao()
    yao.name = "yao"
    ref_a = weakref.ref(yao,call_back)
    return 


if __name__=="__main__":
    run()
    print "finished with no error"
