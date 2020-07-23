# 减色处理 Discretization of Color 有点类似减少锐化
import cv2
import numpy as np

img = cv2.imread("../Question_01_10/imori.jpg")
for i in range(3):
    temp = img[:, :, i]
    temp[np.where((temp >= 0) & (temp < 64))] = 32
    temp[np.where((temp >= 64) & (temp < 128))] = 96
    temp[np.where((temp >= 128) & (temp < 192))] = 160
    temp[np.where((temp >= 192) & (temp < 256))] = 224
cv2.imshow("undefined", img)
cv2.waitKey(0)
