#!/usr/bin/env python

import itertools as it

def number_one ():
    PtGm = 0.04
    PtGw = 0.01

    Pw = 0.6
    Pm = 0.4

    # P( W | T )  = P ( W and T ) / P( T ) = P( W ) * P( T | W) / ( P( W ) * P(T | W) + P( M ) * P( T | M )
    
    top = Pw*PtGw
    bottom = (Pw*PtGw + Pm*PtGm)
    
    print 
    print 'Number one'
    print '{} / {} = {}'.format(top, bottom, top/bottom)

def number_two ():
    # A = Family has children of both sexes
    # B = Family has at most one boy

    A = lambda f: 'B' in f and 'G' in f
    B = lambda f: f.count('B') < 2
    
    print
    print 'Number two'
    
    sexes = ['B', 'G']

    print 'i)'
    families = list( it.product( *[sexes for i in xrange(3)] ) )
    has_both = [f for f in families if A(f) ]
    at_most_1_b = [f for f in families if B(f) ]
    Pa = float(len(has_both))/float(len(families))
    Pb = float(len(at_most_1_b))/float(len(families))
    
    aAb = [f for f in families if A(f) and B(f)]
    PaAb = float(len(aAb)) / float(len(families))
    
    print 'P(A and B) = {}, P(A)P(B) = {}'.format(PaAb, Pa*Pb)
    
    print
    print 'ii)'
    families = list( it.product( *[sexes for i in xrange(2)] ) )
    has_both = [f for f in families if A(f) ]
    at_most_1_b = [f for f in families if B(f) ]
    Pa = float(len(has_both))/float(len(families))
    Pb = float(len(at_most_1_b))/float(len(families))
    
    aAb = [f for f in families if A(f) and B(f)]
    PaAb = float(len(aAb)) / float(len(families))
    
    print 'P(A and B) = {}, P(A)P(B) = {}'.format(PaAb, Pa*Pb)

def number_three ():
    print
    print 'Number three'
    
    Pa = 0.37
    Pb = 0.42
    Pc = 0.21

    PiGa = 0.006
    PiGb = 0.004
    PiGc = 0.012

    # P( c | i )
    top = Pc*PiGc
    bottom = Pa*PiGa + Pb*PiGb + Pc*PiGc
    print '{} / {} = {}'.format(top, bottom, top/bottom)

def number_four ():
    Pd = 0.25
    Pc = 0.75
    
    PfGd = 0.99
    PfGc = 0.17
    
    # P( d | f )
    top = Pd*PfGd
    bottom = Pd*PfGd + Pc*PfGc    

    print
    print 'Number four'
    print '{} / {} = {}'.format(top, bottom, top/bottom)

if __name__ == '__main__':
    number_one()
    number_two()
    number_three()
    number_four()
