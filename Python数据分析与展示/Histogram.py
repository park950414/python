# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:22:57 2017

@author: park
"""

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
mu, sigma = 100, 20
a = np.random.normal(mu, sigma, size=100)

plt.hist(a, 40, normed=1, histtype='stepfilled', facecolor='b',alpha=0.75)
plt.title('Histogram')
plt.savefig("Histogram",dpi=600)
plt.show()