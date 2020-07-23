# 差分滤波器, 也是用于边缘检测， 没有查到相关的资料
#  分为横向和纵向两种算子，纵向值指检测出纵向的边缘，横向指检测横向的边缘
#  主要是用于亮度急剧变化的边缘
import cv2
import numpy as np

vkernel = np.zeros([3, 3])
hkernel = np.zeros([3, 3])
vkernel[1, 1] = 1
vkernel[0, 1] = -1
hkernel[1, 0] = -1
hkernel[1, 1] = 1
img = cv2.imread("../Question_11_20/imori.jpg")
kernel_size = 3
B, G, R = img[:, :, 0], img[:, :, 1], img[:, :, 2]
bw_img = B * 0.0722 + R * 0.2126 + G * 0.7152
res_v_img = np.zeros_like(bw_img)
res_h_img = np.zeros_like(bw_img)
pad_img = np.pad(bw_img, [[1, 1], [1, 1]], "constant", constant_values=0)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        res_v_img[i, j] = np.sum(pad_img[i: i + kernel_size, j: j + kernel_size] * vkernel)
res_v_img = np.clip(res_v_img, 0, 255)
res_v_img = res_v_img.astype(np.uint8)
cv2.imshow("vertical", res_v_img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        res_h_img[i, j] = np.sum(pad_img[i: i + kernel_size, j: j + kernel_size] * hkernel)
res_h_img = np.clip(res_h_img, 0, 255)
res_h_img = res_h_img.astype(np.uint8)
cv2.imshow("horizon", res_h_img)
cv2.waitKey(0)
