# laplacian算子， 求解二次微分检测边缘
# 推导出最后的公式是 x,y的的二阶微分为I(x-1, y) + I(x, y-1) - 4*I(x, y) + I(x+1, y) + I(x, y+1)
import cv2
import numpy as np

kernel = np.array([[0, 1, 0], [1, 4, 1], [0, 1, 0]])
img = cv2.imread("../Question_11_20/imori.jpg")
kernel_size = 3
B, G, R = img[:, :, 0], img[:, :, 1], img[:, :, 2]
bw_img = B * 0.0722 + R * 0.2126 + G * 0.7152
pad_img = np.pad(bw_img, [[1, 1], [1, 1]], "constant", constant_values=0)
res_img = np.zeros_like(bw_img)
for i in range(bw_img.shape[0]):
    for j in range(bw_img.shape[1]):
        res_img[i, j] = np.sum(pad_img[i: i + kernel_size, j: j + kernel_size] * kernel)
res_img = np.clip(res_img, 0, 255).astype(np.uint8)

cv2.imshow("result", res_img)
cv2.waitKey(0)
