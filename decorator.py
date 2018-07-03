#coding:utf-8
'''
实验对装饰器的了解
'''

import time

# def deco(func):
#     startTime = time.time()
#     func()
#     endTime = time.time()
#     msecs = (endTime - startTime) * 1000
#     print "-> elapsed time: {} ms".format( msecs )


# def myfunc():
#     print "start myfunc"
#     time.sleep( 0.6 )
#     print "end myfunc"

# deco(myfunc)

###################################################################

# def deco1(func):
#     def wrapper():
#         startTime = time.time()
#         func()
#         endTime = time.time()
#         msecs = (endTime - startTime) * 1000
#         print "-> elapsed time: {} ms".format( msecs )
#     return wrapper

# def myfunc():
#     print "start myfunc"
#     time.sleep( 0.6 )
#     print "end myfunc"

# print "myfunc is: {}".format( myfunc.__name__)
# myfunc = deco1(myfunc)
# print "myfunc is: {}".format( myfunc.__name__)
# myfunc()

###################################################################

# def deco(func):
#     def wrapper():
#         startTime = time.time()
#         func()
#         endTime = time.time()
#         msecs = (endTime - startTime) * 1000
#         print "-> elapsed time: {} ms".format( msecs )
#     return wrapper

# # 使用了装饰器语法
# # myfunc = deco(myfunc)
# @deco
# def myfunc():
#     print "start myfunc"
#     time.sleep( 0.6 )
#     print "end myfunc"

# print "myfunc is: {}".format( myfunc.__name__ )
# myfunc()



###################################################################

# def wrapper(a, b): <--> myfunc(a, b): 参数一样

# def deco(func):
#     def wrapper(a, b):
#         startTime = time.time()
#         func(a, b)
#         endTime = time.time()
#         msecs = (endTime - startTime) * 1000
#         print "-> elapsed time: {} ms".format( msecs )
#     return wrapper

# # 使用了装饰器语法
# # myfunc = deco(myfunc)
# @deco
# def myfunc(a, b):
#     print "start myfunc"
#     time.sleep( 0.6 )
#     print "end myfunc"

# print "myfunc is: {}".format( myfunc.__name__ )
# myfunc(11, 7)

###################################################################

# 支持任何可变参数的装饰

# def deco(func):
#     def wrapper(*args, **kwargs):
#         startTime = time.time()
#         func(*args, **kwargs)
#         endTime = time.time()
#         msecs = (endTime - startTime) * 1000
#         print "-> elapsed time: {} ms".format( msecs )
#     return wrapper

# # 使用了装饰器语法
# # myfunc = deco(myfunc)
# @deco
# def myfunc(a, b):
#     print "start myfunc a:{} , b:{}".format(a, b)
#     time.sleep( 0.6 )
#     print "end myfunc"

# print "myfunc is: {}".format( myfunc.__name__ )
# myfunc(11, 7)

###################################################################

# 带参数的装饰器

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

# @deco(True)
# def myfunc1(a, b):
#     print "start myfunc a:{} , b:{}".format(a, b)
#     time.sleep( 0.6 )
#     print "end myfunc"

# print "myfunc is: {}".format( myfunc.__name__ )
# myfunc()
# print "myfunc1 is: {}".format( myfunc1.__name__ )
# myfunc1(11, 7)

###################################################################

# # 装饰器的调用顺序
# def deco_1(func):
#     print "enter into deco_1"
#     def wrapper(a, b):
#         print "enter into deco_1 wrapper"
#         func(a, b)
#     return wrapper

# def deco_2(func):
#     print "enter into deco_2"
#     def wrapper(a, b):
#         print "enter into deco_2 wrapper"
#         func(a, b)
#     return wrapper

# @deco_1
# @deco_2
# def addFunc(a, b):
#     print "result is : {}".format( a + b )

# addFunc( 11, 7)



# def main():
#     # deco(myfunc)

#     func = deco1(myfunc)
#     func()

# if __name__ == '__main__':
#     main()
