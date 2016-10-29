# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 08:31:22 2016

##  Plot the curve y = t^2 exp(-t^2) for t values between 0 and 3.

@author: SIDHARTH
"""

import numpy as np
from matplotlib import pyplot as plt
t = np.linspace(0,3,50)
y = (t**2)*np.exp(-t**2)
plot1, = plt.plot(t,y, label='Line')
plt.title("A Skewed Graph")
plt.xlabel("Range")
plt.ylabel("Computed Value")
plt.legend(handles=[plot1])
plt.show()
