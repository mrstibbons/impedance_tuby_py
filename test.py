import numpy as np

for r in np.arange(0.1, 3, 0.1):
    print "new iter"
    for i in np.arange(2.1, 4, 0.1):
        h12 = np.complex(r,i)
        z = np.exp(-1 * h12.imag * 0.5 * 0.1)
        n = np.exp(h12.imag * 0.5 * 0.1)
        f = np.exp(h12.imag * 2 * 0.5 * 0.1)

        print "\th12: ", h12
        print "\tr: ", (h12.real - z) / (n - h12.real) * f
