from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt


sensors = genfromtxt("c:/Users/Ramez Iskandar/Downloads/test_proc/2022-6-14-17-26.csv", delimiter=',')
sensors = np.delete(sensors,0,0)
sensors = np.delete(sensors,np.s_[0:6],1)

#plt.plot(sensors[:,0])
plt.show()
print(np.zeros(2))