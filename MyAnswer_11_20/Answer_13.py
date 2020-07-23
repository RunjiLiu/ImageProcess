#  使用MAX-MIN进行过滤, 进行边缘检测
import cv2
import numpy as np

img = cv2.imread("../Question_11_20/imori.jpg")
kernel_size = 3
B, G, R = img[:, :, 0], img[:, :, 1], img[:, :, 2]
bw_img = B * 0.0722 + R * 0.2126 + G * 0.7152
pad_img = np.pad(bw_img, [[1, 1], [1, 1]], "constant", constant_values=0)
re_noise_img = np.zeros_like(bw_img)
for x in range(bw_img.shape[0]):
    for y in range(bw_img.shape[1]):
            tmp = pad_img[x:x + kernel_size, y: y + kernel_size]
            re_noise_img[x, y] = np.max(tmp) - np.min(tmp)
re_noise_img = np.clip(re_noise_img, 0, 255)
re_noise_img = re_noise_img.astype(np.uint8)
cv2.imshow("reduce noise", re_noise_img)
cv2.waitKey(0)
