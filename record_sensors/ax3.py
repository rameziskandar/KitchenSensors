
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
 
def parser(x):
	return datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')

def parser2(x):
	return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
 
ax3 = pd.read_csv('C:/Users/Ramez Iskandar/Downloads/test_proc/spatula.csv', header=None, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
ax3 = ax3.reset_index()
ax3['Date'] = ax3[0].dt.round('10ms')
#ax3.index = ax3['Date']
#ax3 = ax3.drop(labels=0,axis=1)
#ax3.plot()
#plt.show()
print(ax3)

#['year','month','day','hour','minute','second']
ard = pd.read_csv('C:/Users/Ramez Iskandar/Downloads/test_proc/arduino_data.csv', header=0, parse_dates=['Date'], index_col=0, squeeze=True, date_parser=parser)
ard = ard.reset_index()
ard = ard.drop(labels=0, axis=0)
ard.index = ard['Date'].dt.round('10ms')
#ard = ard.drop(labels='Date', axis=1)

#ard = ard.reset_index()
#ard.plot('Date')
#plt.show()

found = 0
last = 0
ind_ax3 = []
for i in range(len(ard.index)):
	ind = ax3.Date[ax3.Date == ard.index[i]].index.to_list()
	if not ind:
		ind_ax3.append(last+3)
		
	else:
		ind_ax3.append(ind[0])
		last = ind[0]
    #if found == 0:
    #    ind_ax3.append(last)
ax3 = ax3.drop(labels=0,axis=1)
print(ax3)
#ind_ard = []
#for i in range(len(ard['Date'])):
#	if ard['Date'][i] in newindex:
#		ind_ard.append(i)
#ard = ard.drop(labels='Date', axis=1)
#print(ind_ax3)
#ax3 = ax3.reset_index()
#ard = ard.reset_index()
#print(ax3[ind_ax3.value])
#newindex = newindex.dt.round('10ms')
#print(ax3[newindex[1]])
print(ax3)
ax3 = ax3.reindex(ind_ax3)
ax3.index = ax3.Date
ax3 = ax3.drop(labels ='Date', axis=1)
#ard = ard.reindex(ind_ard)
#ard = ard.reindex(newindex)
#print(newindex.shape)
print(ard)
print(ax3)