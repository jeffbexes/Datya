#imports
import matplotlib
import csv
from matplotlib import pyplot as plt
import numpy as np

#interpreter
f=open('data.txt',"r")
lines=f.readlines()
crimes=[]

#reading.moment
for h in lines:
    crimes.append(h.split(' ')[3])
#axis setup
plt.xlim(2000,2019)
plt.ylim(0,1500000)
plt.axline((2000,1425486.00),(2019,1203808.00))
#labeling.exe
plt.xlabel("years")
plt.ylabel("number of crimes, in millions, in the USA")

#moment of coolness
plt.show()
f.close()
