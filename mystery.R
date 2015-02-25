# HW4 marginal probability calculator

# probability domains
domB <- c("b=M","b=!M")
domM <- c("m=M","m=!M")
domK <- c("k=K","k=!K")

# probabilities of B and M
Pb=array(c(0.6,0.4),dimnames=list(domB))
Pm=array(c(0.2,0.8),dimnames=list(domM))

# probability of Pbmk
Pbmk = array( c(.1,.2,.6,.3,.9,.8,.4,.7),
	   c(2,2,2),
	   dimnames<-list(domB,domM,domK) )

# joint probability of independent B,M	   
Pbm = Pb %o% Pm

# P(b=B | k=K) --> marginal P(k=K | b=B,m) / marginal P(k=K | b, m)
#
# mPKBm = marginal P(k=K | b=B,m)
# mPKbm = marginal P(k=K | b, m)
# mPKbm = PK
#
mPKBm = sum(Pbmk["b=M",,"k=K"] * Pbm["b=M",])
PK = sum(Pbmk[,,"k=K"] * Pbm)

PBK = mPKBm/PK
