#!/usr/bin/env python

import itertools as it
import numpy as np

def number_two ():
    
    S = list( it.product( *[['H', 'T'] for i in xrange(3)] ) )
    S.remove(('T', 'T', 'T'))
    S.remove(('H', 'H', 'H'))
    
    head_count = [ numof(s, 'H') for s in S ]
    
    
    
    


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
    #number_seven()
    #number_eight()
