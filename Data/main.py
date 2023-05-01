#imports
import matplotlib
import csv
from matplotlib import pyplot as plt
import numpy as np

#interpreter
f=open('data.txt',"r")
lines=f.readlines()
crimes=[]
years=[]

#reading.moment
for h in lines:
    crimes.append(h.split(' ')[3])
for k in lines:
    years.append(k.split(' ')[0])

#axis setup
k=years
default_k_ticks = range(len(k))
plt.xticks(default_k_ticks, k)

h=crimes
default_h_ticks=range(len(k))
plt.yticks(default_h_ticks,h)

#labeling.exe
'''plt.xlabel("years")
plt.ylabel("number of crimes, in millions, in the USA")'''

#moment of coolness
plt.plot(crimes)
plt.show()
f.close()
