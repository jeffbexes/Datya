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
#work=Force*Distance
xlim=plt.xlim(2000,2019)
ylim=plt.ylim(0,600)
plt.axline((2000,506.50),(2019,366.70), color='blue',label="national average")
plt.axline((2000,151.94),(2019,278.84), color= 'orange', label="new yorks average")
#labeling.exe
plt.xlabel("years")
plt.ylabel("Crimes Rates in the USA")
plt.legend(loc="upper right")


#moment of coolness
plt.show()
f.close()
