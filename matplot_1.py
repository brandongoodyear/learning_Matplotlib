# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:54:18 2019

@author: Brandon Goodyear
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
#%matplotlib inline #for notebook

apl=[93.95,112.15,104.05,144.85,169.49]
price=[39.01,50.29,57.05,69.98,94.39]
year=[2014,2015,2016,2017,2018]

"""
plt.plot(year, apl, '--k',
         year, price, '->y')
#plt.scatter(year,price)
plt.axis([2013,2020,20,180]) #change axis values 

plt.xlabel('year')
plt.ylabel('stock price')

#plt.show() notebook
"""
fig_1=plt.figure(1,figsize=(6.4,4.8)) #6.4 4.8 are default values for size
apl_price=fig_1.add_subplot(1,2,1) #(rows,columns,position)
micro_price=fig_1.add_subplot(1,2,2)

apl_price.plot(year,apl)
micro_price.scatter(year,price)

fig_2,axes=plt.subplots(1,2,figsize=(4,2.5))
axes[0].scatter(year,price)
axes[1].plot(year,apl)
