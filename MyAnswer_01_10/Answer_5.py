# RGB to HSV to RGB
# 除了有RGB空间外，还有HSV(Hue 色相，Saturation 饱和度， 明度 Value)空间也可以用来表示一个图片

import cv2
import numpy as np

img = cv2.imread("../Question_01_10/imori.jpg")
img = img.astype(np.float32)
img = img / 255  # 必须先进行归一化
max_pixel = np.max(img, axis=2)
min_pixel = np.min(img, axis=2)

hsv_img = img.copy()
B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]

# RGB to HSV
hsv_img[:, :, 0][max_pixel == min_pixel] = 0
index = np.where(min_pixel == B)
hsv_img[:, :, 0][index] = 60 * (G[index] - R[index]) / (max_pixel[index] - min_pixel[index]) + 60
index = np.where(min_pixel == R)
hsv_img[:, :, 0][index] = 60 * (B[index] - G[index]) / (max_pixel[index] - min_pixel[index]) + 180
index = np.where(min_pixel == G)
hsv_img[:, :, 0][index] = 60 * (R[index] - B[index]) / (max_pixel[index] - min_pixel[index]) + 300

hsv_img[:, :, 1] = max_pixel - min_pixel

hsv_img[:, :, 2] = max_pixel

hsv_img[:, :, 0] = (hsv_img[:, :, 0] + 180) % 360
# HSV to RGB

C = hsv_img[:, :, 1]
H = hsv_img[:, :, 0] / 60
V = hsv_img[:, :, 2]
X = C * (1 - np.abs(np.mod(H, 2) - 1))

Z = np.zeros_like(H)
vals = [[Z, X, C], [Z, C, X], [X, C, Z], [C, X, Z], [C, Z, X], [X, Z, C]]

rgb_img = hsv_img.copy()

for i in range(6):
    ind = np.where((i <= H) & (H < (i + 1)))
    # 这里有要注意的是公式中各个情况的顺序是按照RGB的顺序来的，但是实际上为了显示应该使用BGR，因此应该第一通道和第三通道互换
    rgb_img[..., 0][ind] = (V - C)[ind] + vals[i][0][ind]
    rgb_img[..., 1][ind] = (V - C)[ind] + vals[i][1][ind]
    rgb_img[..., 2][ind] = (V - C)[ind] + vals[i][2][ind]

max_v = np.max(img, axis=2).copy()
min_v = np.min(img, axis=2).copy()
rgb_img[np.where(max_v == min_v)] = 0  # 根据H的定义当BGR最大值相同时H为0,此时BGR该点为0

rgb_img = np.clip(rgb_img, 0, 1)
rgb_img = (rgb_img * 255).astype(np.uint8)
cv2.imshow("undefined", rgb_img)
cv2.waitKey(0)
