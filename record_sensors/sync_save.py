import matplotlib
matplotlib.use('TkAgg')

import numpy as np
from numpy import genfromtxt
import cv2
import matplotlib.pyplot as plt
import glob
import pandas as pd
fig = plt.figure(figsize=(7, 2))
from datetime import datetime
 

plot_int = 100

path_arduino = 'C:/Users/Ramez Iskandar/Desktop/EPFL/MA4/Semester project - Mathis/KitchenSensors/record_sensors/arduino_data.csv'

path_knife = 'C:/Users/Ramez Iskandar/Desktop/EPFL/MA4/Semester project - Mathis/KitchenSensors/record_sensors/knife.csv'
path_spatula = 'C:/Users/Ramez Iskandar/Desktop/EPFL/MA4/Semester project - Mathis/KitchenSensors/record_sensors/spatula.csv'

def parser(x):
	return datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')

def data_for_plot(ax3): 
    data = np.empty((len(ax3)+int(plot_int),3))
    temp = ax3[1].iloc[:].values
    data[:,0] = np.insert(temp, 0, [temp[0]]*int(plot_int))
    temp = ax3[2].iloc[:].values
    data[:,1] = np.insert(temp, 0, [temp[0]]*int(plot_int))
    temp = ax3[3].iloc[:].values
    data[:,2] = np.insert(temp, 0, [temp[0]]*int(plot_int))
    return data

def sync_ax(path_ax3,ard):
    ax3 = pd.read_csv(path_ax3, header=None, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
    ax3 = ax3.reset_index()
    ax3['Date'] = ax3[0].dt.round('10ms')
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

    ax3 = ax3.drop(labels=0,axis=1)
    ax3 = ax3.reindex(ind_ax3)
    ax3.index = ax3.Date
    ax3 = ax3.drop(labels ='Date', axis=1)
    return ax3

ard = pd.read_csv(path_arduino, header=0, parse_dates=['Date'], index_col=0, squeeze=True, date_parser=parser)
ard = ard.reset_index()
ard = ard.drop(labels=0, axis=0)
ard.index = ard['Date'].dt.round('10ms')
ard = ard.drop(labels ='Date', axis=1)




spatula = sync_ax(path_spatula,ard)
knife = sync_ax(path_knife,ard)


ard_sen1X = ard['sensor1X'].iloc[:].values
ard_sen1X = np.insert(ard_sen1X, 0, [ard_sen1X[0]]*int(plot_int))
ard_sen1Y = ard['sensor1Y'].iloc[:].values
ard_sen1Y = np.insert(ard_sen1Y, 0, [ard_sen1Y[0]]*int(plot_int))
ard_sen1Z = ard['sensor1Z'].iloc[:].values
ard_sen1Z = np.insert(ard_sen1Z, 0, [ard_sen1Z[0]]*int(plot_int))

ard_sen2X = ard['sensor2X'].iloc[:].values
ard_sen2X = np.insert(ard_sen2X, 0, [ard_sen2X[0]]*int(plot_int))
ard_sen2Y = ard['sensor2Y'].iloc[:].values
ard_sen2Y = np.insert(ard_sen2Y, 0, [ard_sen2Y[0]]*int(plot_int))
ard_sen2Z = ard['sensor2Z'].iloc[:].values
ard_sen2Z = np.insert(ard_sen2Z, 0, [ard_sen2Z[0]]*int(plot_int))

ard_sen5X = ard['sensor5X'].iloc[:].values
ard_sen5X = np.insert(ard_sen5X, 0, [ard_sen5X[0]]*int(plot_int))
ard_sen5Y = ard['sensor5Y'].iloc[:].values
ard_sen5Y = np.insert(ard_sen5Y, 0, [ard_sen5Y[0]]*int(plot_int))
ard_sen5Z = ard['sensor5Z'].iloc[:].values
ard_sen5Z = np.insert(ard_sen5Z, 0, [ard_sen5Z[0]]*int(plot_int))

ard_sen6X = ard['sensor6X'].iloc[:].values
ard_sen6X = np.insert(ard_sen6X, 0, [ard_sen6X[0]]*int(plot_int))
ard_sen6Y = ard['sensor6Y'].iloc[:].values
ard_sen6Y = np.insert(ard_sen6Y, 0, [ard_sen6Y[0]]*int(plot_int))
ard_sen6Z = ard['sensor6Z'].iloc[:].values
ard_sen6Z = np.insert(ard_sen6Z, 0, [ard_sen6Z[0]]*int(plot_int))

data_spat = data_for_plot(spatula)
data_knife = data_for_plot(knife)

line1, = plt.plot((data_spat[:plot_int,0]-data_spat[0,0])+5)        # so that we can update data later
line2, = plt.plot((data_spat[:plot_int,1]-data_spat[0,1])+5)        # so that we can update data later
line3, = plt.plot((data_spat[:plot_int,2]-data_spat[0,2])+5)        # so that we can update data later

line4, = plt.plot((data_knife[:plot_int,0]-data_knife[0,0])-5)        # so that we can update data later
line5, = plt.plot((data_knife[:plot_int,1]-data_knife[0,1])-5)        # so that we can update data later
line6, = plt.plot((data_knife[:plot_int,2]-data_knife[0,2])-5)        # so that we can update data later


line7, = plt.plot(ard_sen2X[:plot_int])  
line8, = plt.plot(ard_sen2Y[:plot_int])  
line9, = plt.plot(ard_sen2Z[:plot_int])  

line10, = plt.plot(ard_sen5X[:plot_int])  
line11, = plt.plot(ard_sen5Y[:plot_int])  
line12, = plt.plot(ard_sen5Z[:plot_int])  

line13, = plt.plot(ard_sen6X[:plot_int])  
line14, = plt.plot(ard_sen6Y[:plot_int])  
line15, = plt.plot(ard_sen6Z[:plot_int])  
#plt.vlines(plot_int/2, -10, 10, colors='r')
plt.ylim((-15,15))
plt.grid(True)



for i,filename in enumerate(glob.glob('c:/Users/Ramez Iskandar/Downloads/test_proc/output0/*.png')):
    # update data
    line1.set_ydata((data_spat[i:i+plot_int,0]-data_spat[0,0])+5)
    line2.set_ydata((data_spat[i:i+plot_int,1]-data_spat[0,1])+5)
    line3.set_ydata((data_spat[i:i+plot_int,2]-data_spat[0,2])+5)

    line4.set_ydata((data_knife[i:i+plot_int,0]-data_knife[0,0])-5)
    line5.set_ydata((data_knife[i:i+plot_int,1]-data_knife[0,1])-5)
    line6.set_ydata((data_knife[i:i+plot_int,2]-data_knife[0,2])-5)
    
    line7.set_ydata(ard_sen2X[i:i+plot_int]-ard_sen2X[0])
    line8.set_ydata(ard_sen2Y[i:i+plot_int]-ard_sen2Y[0])
    line9.set_ydata(ard_sen2Z[i:i+plot_int]-ard_sen2Z[0])

    line10.set_ydata(ard_sen5X[i:i+plot_int]-ard_sen5X[0])
    line11.set_ydata(ard_sen5Y[i:i+plot_int]-ard_sen5Y[0])
    line12.set_ydata(ard_sen5Z[i:i+plot_int]-ard_sen5Z[0])

    line13.set_ydata(ard_sen6X[i:i+plot_int]-ard_sen6X[0])
    line14.set_ydata(ard_sen6Y[i:i+plot_int]-ard_sen6Y[0])
    line15.set_ydata(ard_sen6Z[i:i+plot_int]-ard_sen6Z[0])

    # redraw the canvas
    fig.canvas.draw()

    # convert canvas to image
    img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8,
            sep='')
    img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    # img is rgb, convert to opencv's default bgr
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)


    # display image with opencv or any operation you like
    cv2.imshow("plot",img)

    # display camera feed
    frame = cv2.imread(filename)

    height, width, layers = frame.shape
    size = (width/2,height/2)
    resized = cv2.resize(frame, (640,360), interpolation = cv2.INTER_AREA)
    cv2.imshow("cam",resized)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break