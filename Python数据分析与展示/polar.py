# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:33:38 2017

@author: park
"""

import numpy as np
import matplotlib.pyplot as plt

N = 10
theta = np.linspace(0.0, 2*np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 2 * np.random.rand(N)

ax = plt.subplot(111,projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0)
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r/10.0))
    bar.set_alpha(0.5)
    
plt.savefig("polar",dpi=600)
plt.show()