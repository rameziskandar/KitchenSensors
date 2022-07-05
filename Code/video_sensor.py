import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt


img_array = []
for filename in glob.glob("c:/Users/Ramez Iskandar/Downloads/test_proc/output0/*.png"):
    img = cv2.imread(filename)
    cv2.imshow('frame',img)
    cv2.waitKey(3)
    height, width, layers = img.shape
    size = (width,height)
    print(size)
    img_array.append(img)