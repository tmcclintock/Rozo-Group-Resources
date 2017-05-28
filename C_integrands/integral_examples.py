"""
Here we write how to do some integral numerically, and
compare the computational speed.

The integral is \int_\pi^{2\pi} cos(x)/x^3 dx \approx -0.0152115

"""
import numpy as np
import time
from scipy.integrate import quad

def integrand(x):
    return np.cos(x)/x**3

def do_integral():
    return quad(integrand, np.pi, 2*np.pi)

if __name__ == "__main__":
    start = time.time()
    for i in xrange(100000):
        answer = do_integral()
    end = time.time()
    print end - start
