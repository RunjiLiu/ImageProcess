# Emboss滤波器，用来增强轮廓
import cv2
import numpy as np
img = cv2.imread("../Question_11_20/imori.jpg")
B, G, R = img[:, :, 0], img[:, :, 1], img[:, :, 2]
bw_img = B * 0.0722 + R * 0.2126 + G * 0.7152
pad_img = np.pad(bw_img, [[1, 1], [1, 1]], "constant", constant_values=0)
res_img = np.zeros_like(bw_img)
kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
kernel_size = 3
for i in range(bw_img.shape[0]):
    for j in range(bw_img.shape[1]):
        res_img[i, j] = np.sum(pad_img[i: i+kernel_size, j: j+kernel_size] * kernel)
res_img = np.clip(res_img, 0, 255).astype(np.uint8)
cv2.imshow("res", res_img)
cv2.waitKey(0)