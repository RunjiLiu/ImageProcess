#  LoG滤波器， 使用高斯滤波器进行平滑化(去噪)后再使用拉普拉斯滤波器使图像轮廓更加清晰
import cv2
import numpy as np

img = cv2.imread("../Question_11_20/imori_noise.jpg")
kernel_size = 3
kernel = np.zeros([kernel_size, kernel_size])
pad_img = np.pad(img, [[1, 1], [1, 1], [0, 0]], "constant", constant_values=0)
res_img = np.zeros_like(img)
sigma = 0.8
for i in range(-1, 2):
    for j in range(-1, 2):
        kernel[j+1, i+1] = (i**2 + j**2 - sigma**2) / (2*np.pi*sigma**6) * np.exp(-1 * ((i**2 + j**2) / (2*sigma**2)))
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for k in range(img.shape[2]):
            res_img[i, j, k] = np.sum(pad_img[i: i+kernel_size, j: j+kernel_size, k] * kernel)
res_img = np.clip(res_img, 0, 255).astype(np.uint8)
B, G, R = res_img[:, :, 0], res_img[:, :, 1], res_img[:, :, 2]
bw_img = B * 0.0722 + R * 0.2126 + G * 0.7152
pad_img = np.pad(bw_img, [[1, 1], [1, 1]], "constant", constant_values=0)
l_kernel = np.array([[0, 1, 0], [1, 4, 1], [0, 1, 0]])

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        res_img[i, j] = np.sum(pad_img[i: i+kernel_size, j:j+kernel_size] * l_kernel)
res_img = np.clip(res_img, 0, 255).astype(np.uint8)
cv2.imshow("reduce noise", res_img)
cv2.waitKey(0)