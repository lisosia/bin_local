#!/usr/bin/env python

from io import StringIO
import sys
import numpy as np
from pylab import *
import re
import math, scipy.optimize

# when A=1, integral gaussian() = 1
def gaussian(x, A, mean, sigma):
    gauss = A/math.sqrt(2.0*math.pi)/sigma * np.exp(-((x-mean)/sigma)**2/2)
    return(gauss)

def f_errors(param_fit, x, y, yerr):
    mean, sigma = param_fit
    base = 0.0
    err = (y - (gaussian(x, 1, mean, sigma) + base) ) / yerr
    return(err)

def gauss_fit(x,y):
    param0 = [1.0e-9,1.0e-9 ] # initial guess
    param_output = scipy.optimize.leastsq(f_errors, param0, args=(x, y, 1.0 ), full_output=True)
    param_result = param_output[0] # fitted parameters
    covar_result = param_output[1] # covariant matrix   )
    return [param_result, covar_result]
def main():
    X = np.arange( 0., 100., 1.)
    Y = gaussian( X, 1. , 30. , 10.  ) 
    Y += 0.1* np.mean(Y) * np.random.randn(len(X))

    print gauss_fit(X,Y)[0]
    import pylab
    plot(X,Y)
    # show()

if __name__=="__main__":
    main()
