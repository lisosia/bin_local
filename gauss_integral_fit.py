#!/usr/bin/env python

from io import StringIO
import sys
import numpy as np
from pylab import *
import re
import math, scipy.optimize

from scipy.special import erf

def gauss_int(x, mean, sigma ):
    return ( 0.5 + 0.5 * erf( (x-mean) /sigma ) )

#alternative
#from scipy.stats import norm
#print norm.cdf(0.0)

def f_errors(param_fit, x, y, inc ):
    if not inc: # if y is descreasing ; [0.9,0.5,0.1] convert to  [0.1, 0.5, 0.9]
        y = 1.0 - y
    mean, sigma = param_fit
    err = (y - (gauss_int(x, mean, sigma) ) )
    return err

def gauss_int_fit(x,y, param0 = [1.0e-9,10.0e-9 ], inc=True ):
    # param0 : initial guess of means,signma
    param_output = scipy.optimize.leastsq(f_errors, param0, args=(x, y, inc ), full_output=True)

    param_result = param_output[0] # fitted parameters
    covar_result = param_output[1] # covariant matrix   )
    return param_output

def main():
    X = np.arange( 0., 100., 1.)
    Y = gaussian( X, 1. , 30. , 10.  ) 
    Y += 0.1* np.mean(Y) * np.random.randn(len(X))

    print gauss_fit(X,Y)[0]
    import pylab
    plot(X,Y)
    show()

if __name__=="__main__":
    main()
