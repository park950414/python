# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:21:45 2017

@author: park
"""
import matplotlib.pyplot as plt
plt.plot([3,1,4,5,2])
plt.ylabel("纵轴（值）",fontproperties='SimHei',fontsize=20)
plt.savefig('test3',dpi=600)
plt.show()