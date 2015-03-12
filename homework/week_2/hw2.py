#!/usr/bin/env python

import itertools as it
import numpy as np
from scipy.misc import comb

def number_two ():
    
    head_filter = lambda x: x == 1 or x == 2
    
    flips = list( it.product( *[['H', 'T'] for i in xrange(3)] ) )
    
    heads_and_tails = [ f for f in flips if head_filter(numof(f,'H')) ]
    
    one_head = [f for f in heads_and_tails if numof(f, 'H') == 1]
    
    top = float(len(one_head))
    bottom = float(len(heads_and_tails))
    print 'Number 4.32'
    print '{} / {} = {}'.format(top, bottom, top/bottom)

    print 
    print 'flips'
    for i,f in enumerate(flips): print '  {}:{}'.format(i,f)
    print 'heads_and_tails'
    for i,f in enumerate(heads_and_tails): print '  {}:{}'.format(i,f)
    print 'one head'
    for i,f in enumerate(one_head): print '  {}:{}'.format(i,f)
    print 
    
    
def number_three ():
    die = range(1,7)
    
    rolls = list( it.permutations(die, 2) )

    sums = [ sum(r) % 2 for r in rolls ]
    
    print 'Number 4.33'
    top = float(numof(sums, 0))
    bottom = float(len(sums))
    print '{} / {} = {}'.format(top, bottom, top/bottom)
    
def number_four ():
    top =  float(len(list(it.combinations(range(13), 5))))
    bottom = float(len(list(it.combinations(range(26), 5))))

    print 'Number 4.36'
    print '{} / {} = {}'.format(top, bottom, top/bottom)

def number_five ():
    top = comb(10,4) + comb(10,3)*comb(39,1) + comb(10,2)*comb(39,2)
    bottom = comb(49,4)
    
    print 'Number 4.37'
    print '{} / {} = {}'.format(top, bottom, top/bottom)

def number_six ():
    nums = range(1,10)
    rolls = list(it.permutations(nums, 2))

    print 'Number 4.36'
    odd = [r for r in rolls if sum(r)%2 == 1]
    has_2 = [r for r in odd if 2 in r]
    top = float(len(has_2))
    bottom = float(len(odd))
    print '  (i)'
    print '  {} / {} = {}'.format(top, bottom, top/bottom)
    
    has_2 = [r for r in rolls if 2 in r]
    odd = [r for r in has_2 if sum(r)%2 == 1]
    top = float(len(odd))
    bottom = float(len(has_2))
    print
    print '  (ii)'
    print '  {} / {} = {}'.format(top, bottom, top/bottom)
    
def numof (seq, val):
    c = 0
    for e in seq:
        if e == val: c += 1
    return c

def consect (seq, val):
    cur_max = 0
    prev_max = 0
    for e in seq:
        if e == val: prev_max += 1
        else:
            cur_max = max(cur_max, prev_max)
            prev_max = 0
    return max(cur_max, prev_max)

def number_seven ():
    print 'Number 5.44'
    flips = list(it.product(['H','T'],['H','T'],['H','T'],['H','T']))

    X = {k:0 for k in range(5)}
    Y = {k:0 for k in range(5)}
    
    for seq in flips: X[numof(seq, 'H')] += 1
    for seq in flips: Y[consect(seq, 'H')] += 1

    for k,v in X.iteritems():
        X[k] = float(v)/float(len(flips))
    

    for k,v in Y.iteritems():
        Y[k] = float(v)/float(len(flips))

    joint = np.zeros((5,5))
    for seq in flips:
        i = numof(seq, 'H')
        j = consect(seq, 'H')
        
        joint[i,j] += 1
    
    joint /= len(flips)
    
    expected = 0.
    for i in xrange(5):
        for j in xrange(5):
            expected += i*j*joint[i,j]
    print 'expected value: ', expected
    
def number_eight ():
    print 'Number 5.45'
    box = [1, 1, 2, 2, 3]
    
    draws = list(it.permutations(box, 2))
    
    #print ', '.join(['({},{})'.format(i,j) for i,j in draws])

    X = {k:0. for k in range(2,6)}
    Y = {k:0. for k in range(1,4)}
    
    joint = np.zeros((6,4))

    for d in draws:
        i = sum(d)
        j = max(d)
        X[i] += 1.
        Y[j] += 1.
        joint[i,j] += 1.
    
    for k,v in X.iteritems():
        X[k] = float(v)/float(len(draws))
    
    for k,v in Y.iteritems():
        Y[k] = float(v)/float(len(draws))

    joint /= float(len(draws))
    
    expected = 0.
    for i in xrange(2,6):
        for j in xrange(1,4):
            expected += i*j*joint[i,j]
    print 'expected value: ', expected

if __name__ == '__main__':
    number_two()
    number_three()
    number_four()
    number_five()
    number_six()
    #number_seven()
    #number_eight()
