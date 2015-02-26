#!/usr/bin/env python

import numpy as np

def main():
    # States
    knife, maid, butler = 0, 1, 2
    murderer, notmurderer = 0, 1
    used, notused = 0, 1
    
    # Domains
    DB = [murderer, notmurderer]
    DM = [murderer, notmurderer]
    DK = [used, notused]

    # marginal distributions
    # [murderer, not murder]
    Pb = [0.6, 0.4]
    Pm = [0.2, 0.8]
    
    # joint distribution for P( K | B and M )
    #PkGbAm[Knife state][Butler state][Maid state]
    PkGbAm = [[[None for k in DM]for j in DB] for i in DK]
    PkGbAm[used][murderer][murderer] = 0.1
    PkGbAm[used][murderer][notmurderer] = 0.6
    PkGbAm[used][notmurderer][murderer] = 0.2
    PkGbAm[used][notmurderer][notmurderer] = 0.3
    PkGbAm[notused][murderer][murderer] = 0.9
    PkGbAm[notused][murderer][notmurderer] = 0.4
    PkGbAm[notused][notmurderer][murderer] = 0.8
    PkGbAm[notused][notmurderer][notmurderer] = 0.7
    
    # joint probability of P( B and M )
    # bs and ms are the butler state and maid state
    PbAm = [[ Pb[bs]*Pm[ms] for ms in DM ] for bs in DB]
    
    numerator = Pb[murderer]*sum([PkGbAm[used][murderer][ms]*Pm[ms] for ms in DM])
    denominator = sum([Pb[bs] * sum([PkGbAm[used][bs][ms]*Pm[ms] for ms in DM]) for bs in DB])
    
    print
    print '    p(B) sigma( p(K|B,m) * p(m)'
    print '------------------------------------  =  {}'.format(numerator/denominator)
    print ' sigma( p(b) sigma( p(K|b,m) * p(m)'
    print 
    
if __name__ == '__main__':
    main()
