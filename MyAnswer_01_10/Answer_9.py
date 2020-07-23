# 使用高斯滤波进行过滤
import cv2
import numpy as np

img = cv2.imread("../Question_01_10/imori_noise.jpg")  # 带有噪声的图片
cv2.imshow("noise img", img)

kernel = np.zeros([3, 3])
kernel_size = 3
sigma = 1.3
for x in range(-1, 2):  # 高斯滤波器的位置跟平常矩阵从（0,0）开始不同，以中心点为（0,0），向上-1,向左-1, 因此左上角点坐标为(-1,-1)，右下角坐标为（1,1）
    for y in range(-1, 2):
        kernel[y + 1, x + 1] = 1 / 2 / np.pi / (sigma ** 2) * np.exp(-1 * (x ** 2 + y ** 2) / 2 / (sigma ** 2))
# 注意这里归一化有两种
kernel1 = kernel / np.sum(kernel)  # 第一种是全局求和归一化
kernel2 = kernel / kernel[0, 0]  # 第二种是将矩阵左上角元素的倒数作为归一化系数，即将做左上角元素化作1， 之后取整， 乘上矩阵元素之和
kernel2 = kernel2.astype(np.uint8)
kernel2 = kernel2 / kernel2.sum()
# 这种方式求出来的kernel和教程中的不一样，但是当sigma为0.8时，与教程中sigma为1.3的一致, 但算出来的滤波是基本一致的
re_noise_img = np.zeros_like(img)
pad = 1
pad_img = np.pad(img, [[1, 1], [1, 1], [0, 0]], "constant", constant_values=(0, 0))
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        for z in range(img.shape[2]):
            re_noise_img[x, y, z] = np.sum(np.multiply(kernel2, pad_img[x:x + kernel_size, y: y + kernel_size, z]))
re_noise_img = np.clip(re_noise_img, 0, 255)
re_noise_img = re_noise_img.astype(np.uint8)
cv2.imshow("reduce noise", re_noise_img)
cv2.waitKey(0)
