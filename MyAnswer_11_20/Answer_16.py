# prewitt滤波器
import cv2
import numpy as np

vkernel = np.zeros([3, 3])
hkernel = np.zeros([3, 3])
vkernel[0, :] = np.array([-1, -1, -1])
vkernel[2, :] = np.array([1, 1, 1])

hkernel[:, 0] = np.array([-1, -1, -1])
hkernel[:, 2] = np.array([1, 1, 1])
img = cv2.imread("../Question_11_20/imori.jpg")
kernel_size = 3
B, G, R = img[:, :, 0], img[:, :, 1], img[:, :, 2]
bw_img = B * 0.0722 + R * 0.2126 + G * 0.7152
pad_img = np.pad(bw_img, [[1, 1], [1, 1]], "constant", constant_values=0)
vimg = np.zeros_like(bw_img)
himg = np.zeros_like(bw_img)
for i in range(bw_img.shape[0]):
    for j in range(bw_img.shape[1]):
        vimg[i, j] = np.sum(pad_img[i: i + kernel_size, j: j + kernel_size] * vkernel)
for i in range(bw_img.shape[0]):
    for j in range(bw_img.shape[1]):
        himg[i, j] = np.sum(pad_img[i: i + kernel_size, j: j + kernel_size] * hkernel)

himg = np.clip(himg, 0, 255).astype(np.uint8)
vimg = np.clip(vimg, 0, 255).astype(np.uint8)
cv2.imshow("horizon", himg)
cv2.imshow("vertical", vimg)
cv2.waitKey(0)
