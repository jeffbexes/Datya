#imports
import matplotlib
import csv
from matplotlib import pyplot as plt

#interpreter
f=open('data.txt',"r")
lines=f.readlines()
crimes=[]
years=[]
for y in lines:
    crimes.append(y.split(' ')[1])
for x in lines:
    years.append(x.split(' ')[0])
x=years
default_x_ticks = range(len(x))
plt.xticks(default_x_ticks, x)
    

plt.plot(crimes)
plt.plot(crimes)
plt.show()
f.close()