# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 17:41:27 2015

@author: davidkohn
"""

x = 0.1
s = x/2
tol = 1.e-14
kmax=10000
for k in range(kmax) :
    print "Before iteration %s, s = %s" %(k,s)
    s0 = s
    s = 0.5 * (s+x/s)
    k = k+1
    
    if abs((s-s0)/s)<tol:
        break
    

print "After %s iterations s = %s" %(k,s)

