import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread("../Question_11_20/imori_dark.jpg").astype(np.float32)
print(img.shape)
img2 = img.ravel()
print(img2.shape)
plt.hist(img2, bins=255, range=(0, 255), rwidth=0.8)
# bins标记了有255个直柱，range标识了横轴的范围, rdith标识了直柱间的距离, 越小柱越细， 柱间距离越大，默认为0
# 直方图显示出了每个不同像素值出现的次数
plt.show()