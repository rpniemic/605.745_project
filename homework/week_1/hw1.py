#!/usr/bin/env python

import math

def number_3 ():

    print 
    print 'Distribution 1'
    
    d1 = [ [2., 3., 11.],
           [1./3., 1./2., 1./6.] ]
    
    mu = mean(d1)
    print '  mu: {}'.format(mu)
    
    sig2 = var(d1, mu)
    print '  Variance: {}'.format(sig2)
    
    sig = math.sqrt(sig2)
    print '  Std Dev: {}'.format(sig)

    print
    print 'Distribution 2'
    d2 = [ [-5., -4., 1., 2.],
           [1./4., 1./8., 1./2., 1./8.] ]

    mu = mean(d2)
    print '  mu: {}'.format(mu)
    
    sig2 = var(d2, mu)
    print '  Variance: {}'.format(sig2)
    
    sig = math.sqrt(sig2)
    print '  Std Dev: {}'.format(sig)

    print
    print 'Distribution 3'
    d3 = [ [1., 3., 4., 5.],
           [.4, .1, .2, .3] ]
    
    mu = mean(d3)
    print '  mu: {}'.format(mu)
    
    sig2 = var(d3, mu)
    print '  Variance: {}'.format(sig2)
    
    sig = math.sqrt(sig2)
    print '  Std Dev: {}'.format(sig)
    
def number_4 ():
    die = [ [float(v) for v in xrange(1,7)],
            [1./6. for i in xrange(6)] ]
    
    X = lambda x: 2*x
    Y = lambda y: 1. if y%2 != 0 else 3.
    
    x_space = [ [X(xi) for xi,_ in zip(*die)],
                [pi for _,pi in zip(*die)] ]
    
    y_space = [ [1., 3.],
                [1./2., 1./2.] ]

    print
    print 'X'
    for xi, pi in zip(*x_space): print '  x_i: {}, p_i: {}'.format(xi,pi)
    print '  Expectation: {}'.format(mean(x_space))
    print '  Std Dev: {}'.format(math.sqrt(var(x_space, mean(x_space))))
    
    print 
    print 'Y'
    for xi, pi in zip(*y_space): print '  x_i: {}, p_i: {}'.format(xi,pi)
    print '  Expectation: {}'.format(mean(y_space))
    print '  Std Dev: {}'.format(math.sqrt(var(y_space, mean(y_space))))
    
    x_p_y_space = [ [X(xi)+Y(xi) for xi,_ in zip(*die)],
                    [pi for _,pi in zip(*die)] ]

    print
    print 'X + Y'
    for xi, pi in zip(*x_p_y_space): print '  x_i: {}, p_i {}'.format(xi,pi)
    print '  Expectation: {}'.format(mean(x_p_y_space))
    print '  Std Dev: {}'.format(math.sqrt(var(x_p_y_space, mean(x_p_y_space))))
    
    x_t_y_space = [ [X(xi)*Y(xi) for xi,_ in zip(*die)],
                    [pi for _,pi in zip(*die)] ]

    print
    print 'XY'
    for xi, pi in zip(*x_t_y_space): print '  x_i: {}, p_i: {}'.format(xi,pi)
    print '  Expectation: {}'.format(mean(x_t_y_space))
    print '  Std Dev: {}'.format(math.sqrt(var(x_t_y_space, mean(x_t_y_space))))
    
def mean (space):
    return sum([xi*pi for xi, pi in zip(*space)])
    
def var (space, mu):
    return sum( [ pi*(xi**2) for xi, pi in zip(*space)] ) - mu**2

if __name__ == '__main__':
    #number_3()
    number_4()
