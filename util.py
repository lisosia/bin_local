#!/usr/bin/env python

from io import StringIO
import sys
import numpy as np
from pylab import *
import re

def float_u(s):
#    if re.match( r"^-?\d+\.?(\d+)?$|^-?\d+([eE][+-]?)", s ):
    if re.match( r"^-?\d+(\.\d+)?([eE][+-]?\d+)?$", s ):
        return np.float( s )
    elif re.match( r"\d+.*p$", s ):
        return np.float( s[0:-1] ) * 1.0e-12
    elif re.match( r"-?\d+.*n$", s ):
        return np.float( s[0:-1] ) * 1.0e-9
    elif re.match( r"-?\d+.*m$", s ):
        return np.float( s[0:-1] ) * 1.0e-3
    elif re.match( r"-?\d+.*k$", s ):
        return np.float( s[0:-1] ) * 1.0e+3
    elif re.compile( r"(\d+.*)mega?$" ).search( s ):
        m = re.compile( r"(\d+.*)mega?$" ).search( s )
        return np.float( m.group(1) ) * 1.0e+6
    elif re.match( r"\d+.*g$", s ):
        return np.float( s[0:-1] ) * 1.0e+9
    raise Exception( "convet err %s" % s )

def get_deriv(x ,y ):
    assert len(x) == len(y)
    dx = np.array([])
    dy = np.array([])
    for i in range(0, len(x)-1 ):
        xdiff = x[i+1] - x[i]
        xmean = ( x[i+1] + x[i] ) /2.0
        assert ( xdiff > 0 )
        ydiff = y[i+1] - y[i]
        dx = np.append( dx, xmean )
        dy = np.append( dy, ydiff / xdiff )
    return [dx, dy]
