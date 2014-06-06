#! /usr/bin/env python
from __future__ import division


def doCalculate(first, second, result):
    firstLen = len(first)
    secondLen = len(second)
    if (1 == firstLen):
        if 1 == secondLen:
            fstval = first[0]
            secval = second[0]
            print 'fstval:%d, secval:%d, result:%d' % (fstval, secval, result)
            res = fstval + secval
            if res == result:
                return '(%d + %d)' % (fstval, secval)
            res = fstval * secval
            if res == result:
                return '(%d * %d)' % (fstval, secval)
            res = fstval - secval
            if res == result:
                return '(%d - %d)' % (fstval, secval)
            res = secval - fstval
            if res == result:
                return '(%d - %d)' % (secval, fstval)
            res = fstval / secval
            if res == result:
                return '(%d / %d)' % (fstval, secval)
            res = secval / fstval
            if res == result:
                return '(%d / %d)' % (secval, fstval)
            return ''
        elif 2 == secondLen:
            fstval = first[0]
            res = doCalculate([second[0]], [second[1]], result - fstval)
            if res:
                return '(%d + %s)' % (fstval, res)
            res = doCalculate([second[0]], [second[1]], result / fstval)
            if res:
                return '(%d * %s)' % (fstval, res)
            res = doCalculate([second[0]], [second[1]], fstval - result)
            if res:
                return '(%d - %s)' % (fstval, res)
            res = doCalculate([second[0]], [second[1]], fstval + result)
            if res:
                return '(%s - %d)' % (res, fstval)
            res = doCalculate([second[0]], [second[1]], fstval / result)
            if res:
                return '(%d / %s)' % (fstval, res)
            res = doCalculate([second[0]], [second[1]], fstval * result)
            if res:
                return '(%s / %d)' % (res, fstval)
            return ''
        elif 3 == secondLen:
            fstval = first[0]
            plusTarget = result - fstval
            multiplyTarget = result / fstval
            minusTarget1 = fstval - result
            minusTarget2 = fstval + result
            divideTarget1 = fstval / result
            divideTarget2 = fstval * result
            for i in second:
                copySeconds = second[:]
                copySeconds.remove(i)
                res = doCalculate([i], list(copySeconds), plusTarget)
                if res:
                    return '%d + %s' % (fstval, res)
                res = doCalculate([i], list(copySeconds), multiplyTarget)
                if res:
                    return '%d * %s' % (fstval, res)
                res = doCalculate([i], list(copySeconds), minusTarget1)
                if res:
                    return '%d - %s' % (fstval, res)
                res = doCalculate([i], list(copySeconds), minusTarget2)
                if res:
                    return '%s - %d' % (res, fstval)
                res = doCalculate([i], list(copySeconds), divideTarget1)
                if res:
                    return '%d / %s' % (fstval, res)
                res = doCalculate([i], list(copySeconds), divideTarget2)
                if res:
                    return '%s / %d' % (res, fstval)
                return ''



def calculate(params, targetResult = 24):
    for i in params:
        copyparams = params[:]
        copyparams.remove(i)
        res = doCalculate([i], list(copyparams), targetResult)
        if res:
            return res
    return ''

def main():
    import sys
    if len(sys.argv) != 5:
        print 'usage: ./twenty-four [1-10] [1-10] [1-10] [1-10]'
        return -1
    params = sys.argv[1:]
    for i in range(len(params)):
        try:
            params[i] = int(params[i])
        except ValueError, e:
            print 'Invalid argument:%s' % params[i]
            return -1
    paramError = False
    for i in params:
        if i < 1 or i > 10:
            paramError = True 
            print 'only accept num in [1-10], the value is:',i
    if paramError:
        return -1
    res = calculate(list(params))
    if res:
        print res
    else:
        print 'Input numbers can not calculate the target result 24!'




if __name__ == '__main__' :
    main()

