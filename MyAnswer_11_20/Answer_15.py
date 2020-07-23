# sobel算子，边缘检测， 也是分为横向和纵向
# 如果图片中亮度变化不明显，则sobel的效果会比差分算子好
# 如果在一个区域内， 图像的亮度差别不大（黑白照片用亮度为度量）， sobel算子卷积的结果接近于0, 第一行和第三行互反， 且第二行全为0
# 但是如果在一个存在边缘的区域内， 且假设刚好边缘落在第一行, 则此时的卷积和结果会是最大的， 因为边缘与便边缘两侧有较大差值
# 如果实落在第二行， 则边缘被忽略， 如果边缘两侧亮度同样差距不大， 则比情况一小
# 如果落在第三行，则此时是负数的原因， 是最小的
# 因此sobel无法检测到边缘的两边， 即只有边缘的一侧是亮的
# 此处可以卷积后求个绝对值， 就可以检测到边缘两侧
# sobel算子是prewitt的改进版
import cv2
import numpy as np

vkernel = np.zeros([3, 3])
hkernel = np.zeros([3, 3])
vkernel[0, :] = np.array([1, 2, 1])
vkernel[2, :] = np.array([-1, -2, -1])

hkernel[:, 0] = np.array([1, 2, 1])
hkernel[:, 2] = np.array([-1, -2, -1])
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
