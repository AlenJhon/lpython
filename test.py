#coding:utf-8
# 对python中yield探索

def gen(n):
    for i in n:
        yield i * 2

def for_dict():
    tdict = {"a":11, "b":22}
    for key,val in tdict.items():
        print key, val

def ret_list():
    return 1,2,3

def main():
    # print 'Hello World!'
    # # tmp = gen(2)
    # for x in gen([1,2]):
    #     print x
    # for_dict()
    # a,b = ret_list()
    # print a
    # print b

    mylist = [1, 2, 3, 4]
    print "|".join( mylist )
    

def add(x,y):
    return x+y

if __name__ == '__main__':
    main()