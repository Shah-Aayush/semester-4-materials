#!/usr/bin/env python3

import random
import numpy
from matplotlib import pyplot as plt

index = [i for i in range(10)]

#india = [random.randint(0,200) for run in range(10)]
#england = [random.randint(0,200) for run in range(10)]

india = [5, 35, 24, 0, 99, 1, 35, 15, 27, 14]
england = [10, 55, 34, 21, 2, 7, 118, 29, 32, 10]

print(index,"\n",india,"\n",england)

plt.plot(index,numpy.cumsum(india),'red',label = 'Line one' , linewidth = 2,marker = 'o')
plt.plot(index,numpy.cumsum(england),'blue',label = 'Line two' , linewidth = 2,marker = 'o')

plt.title('Performance')
plt.ylabel('Runs')
plt.xlabel('Wickets')

plt.legend(["India","England"])

plt.show()