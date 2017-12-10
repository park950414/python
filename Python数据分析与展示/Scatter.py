# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:46:33 2017

@author: park
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.plot(10*np.random.randn(100),10*np.random.randn(100),'o')
ax.set_title('Simple Scatter')
plt.savefig("Scatter",dpi=600)
plt.show()