# 平均池化，可用来进行模糊处理

import cv2
import numpy as np

img = cv2.imread("../Question_01_10/imori.jpg")
img = img.astype(np.float32)
pool_img = np.zeros([16, 16, 3])
for x in range(16):
    for y in range(16):
        pool_img[x, y, :] = np.mean(img[x * 8:(x + 1) * 8, y * 8:(y + 1) * 8:], axis=(0, 1))
pool_img = pool_img.astype(np.uint8)
cv2.imshow("undefined", pool_img)
cv2.waitKey(0)
