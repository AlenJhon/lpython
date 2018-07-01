#coding:utf-8
# 对python中yield探索

def gen(n):
    for i in n:
        yield i * 2

def main():
    print 'Hello World!'
    # tmp = gen(2)
    for x in gen([1,2]):
        print x
    

def add(x,y):
    return x+y

if __name__ == '__main__':
    main()