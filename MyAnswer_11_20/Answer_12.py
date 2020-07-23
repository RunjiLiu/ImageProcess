# 使用Motion Filter进行运动模糊， 会产生一种因运动造成的模糊效果
import cv2
import numpy as np

img = cv2.imread("../Question_11_20/imori.jpg")
kernel_size = 3
kernel = np.eye(kernel_size) / kernel_size
pad_img = np.pad(img, [[1, 1], [1, 1], [0, 0]], "constant", constant_values=0)
re_noise_img = np.zeros_like(img)
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        for z in range(img.shape[2]):
            re_noise_img[x, y, z] = np.sum(pad_img[x: x + kernel_size, y: y + kernel_size,
                                           z] * kernel)
re_noise_img = np.clip(re_noise_img, 0, 255)
cv2.imshow("reduce noise", re_noise_img)
cv2.waitKey(0)
