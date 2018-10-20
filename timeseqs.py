#coding:utf-8
import time, sys
reps_time = 1000
repslist_time = range(reps_time)

def timer(func, *pargs, **kargs):
    start = time.clock()
    for i in repslist_time:
        ret = func(*pargs, **kargs)
    elapsed = time.clock() -start
    return (elapsed, ret)


reps = 10000
repslist = range(reps)

def forLoop():
    res = []
    for x in repslist:
        res.append( abs(x) )
    return res

def listComp():
    return [ abs(x) for x in repslist ]

def mapCall():
    return list(map(abs, repslist))

def genExpr():
    return list(abs(x) for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())


def main():
    print (sys.version)
    for test in (forLoop, listComp, mapCall, genExpr, genFunc):
        elapsed, result = timer(test)
        print ('-' * 33)
        print ('%-9s: %.5f => [%s...%s]' %(test.__name__, elapsed, result[0], result[-1]))

if __name__ == '__main__':
    main()


'''
2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)]
---------------------------------
forLoop  : 1.06229 => [0...9999]
---------------------------------
listComp : 0.54423 => [0...9999]
---------------------------------
mapCall  : 0.48740 => [0...9999]
---------------------------------
genExpr  : 0.70822 => [0...9999]
---------------------------------
genFunc  : 0.70623 => [0...9999]
'''