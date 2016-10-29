# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 08:16:21 2016

Write a function to evaluate y(t) and y'(t) where : y(t) = v0t + (1/2)gt^2, and y'(t) = v0 - gt .

@author: SIDHARTH
"""

import numpy as np
from matplotlib import pyplot as plt
# t = np.linspace(0,5,50)
# g = 9.81
v0 = eval(input('Input Initial Velocity in m/s \n'))
t1 = eval(input('Input Time Range in seconds \n'))
a = eval(input('Input Acceleration in m/s2 \n'))
t = np.linspace(0,t1,50)
dist = v0*t + 0.5*a*t**2
velo = v0 + a*t
plt.plot(2)
plot2, = plt.plot(t,dist, label='Distance')
plot3, = plt.plot(t,velo, label='Velocity')
plt.xlabel('Time s')
plt.ylabel('Distance m')
plt.title('Time Vs Distance/Velocity')
plt.legend(handles = [plot2,plot3])
plt.show()