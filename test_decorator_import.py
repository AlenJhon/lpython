#coding:utf-8
'''
目的：
    为了弄清import的时候装饰器做了什么

结果：
    import进来的时候装饰器都执行过了,

执行程度 ： 
    执行到被修饰的函数被记录下来那一层

时间 ：
    2018-07-04 00点57分

环境：
    window 10   visual studio code

====>>>>>>>比如：

def deco(arg = True):
    if arg:
        def _deco(func):
            def wrapper(*args, **kwargs):
                    startTime = time.time()
                    func(*args, **kwargs)
                    endTime = time.time()
                    msecs = (endTime - startTime) * 1000
                    print "-> elapsed time: {} ms".format( msecs )
            return wrapper
    else:
        print "enter arg is false"
        def _deco(func):
            print "enter _deco arg is false"
            return func
    return _deco

@deco(False)
def myfunc():
    print "start myfunc "
    time.sleep( 0.6 )
    print "end myfunc"

====>>>>>>>在执行import之后打印出来的结果

enter arg is false
enter _deco arg is false

上面所说的那一层就是装饰器里面的要能知道 myfunc这个函数为止


'''

import decorator





def main():
    pass

if __name__ == '__main__':
    main()