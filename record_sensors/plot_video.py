import matplotlib
matplotlib.use('TkAgg')

import numpy as np
from numpy import genfromtxt
import cv2
import matplotlib.pyplot as plt
import glob

fig = plt.figure(figsize=(7, 2))


sensors = genfromtxt("c:/Users/Ramez Iskandar/Downloads/test_proc/output0.csv", delimiter=',')
sensors = np.delete(sensors,0,0)
sensors = np.delete(sensors,np.s_[0:6],1)

print(sensors.shape)

data = sensors[:,3]
data = np.insert(data, 0, [data[0]]*50)
#data = np.insert(data, )
line1, = plt.plot(data[:100])        # so that we can update data later
plt.vlines(50, -10, 10, colors='r')
plt.ylim((-10,10))
plt.grid(True)


for i,filename in enumerate(glob.glob('c:/Users/Ramez Iskandar/Downloads/test_proc/output0/*.png')):
    # update data
    line1.set_ydata(data[i:i+100])

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