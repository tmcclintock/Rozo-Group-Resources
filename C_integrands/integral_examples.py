"""
Here we write how to do some integral numerically, and
compare the computational speed.

The integral is \int_\pi^{2\pi} cos(x)/x^3 dx \approx -0.0152115

"""
import numpy as np
import time
from scipy.integrate import quad
import ctypes
lib = ctypes.cdll.LoadLibrary("integrand.so")
c_integrand = lib.integrand
c_integrand.argtypes = (ctypes.c_int, ctypes.c_double)
c_integrand.restype  = ctypes.c_double

def integrand(x):
    return np.cos(x)/x**3

def do_integral():
    return quad(integrand, np.pi, 2*np.pi)

def do_c_integral():
    return quad(c_integrand, np.pi, 2*np.pi)

if __name__ == "__main__":
    print "Python version:", do_integral()
    print "ctypes version:", do_c_integral()

    start = time.time()
    for i in xrange(100000):
        answer = do_integral()
    end = time.time()
    print end - start, "For python version"
    start = time.time()
    for i in xrange(100000):
        answer = do_c_integral()
    end = time.time()
    print end - start, "For c_types version"
