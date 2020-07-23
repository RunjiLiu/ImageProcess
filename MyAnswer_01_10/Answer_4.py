# 二值化 自动确定阀值
import cv2
import numpy as np

# 确定一个阀值t，使得类内方差（同属于一个类内的方差）比类间方差（两个类之间的方差）最大化
# 类内方差=0类占比×0类的类内方差（（0类各数据点-均值）的平方）+1类占比×1类的类内方差
# 类间方差=0类占比×0类的类间方差（（0类均值-总体均值）的平方）+1类占比×1类的类间方差=0类占比×1类占比×（（0类均值-1类均值）的平方）
# 目的是二值化的效果最好，就是让类内方差尽可能小，类间方差尽可能大，即让类间方差/类内方差的值尽可能大，该式等价于类间方差/（总方差-类间方差）
# 因为类间方差与类内方差的和为一个常数，故求解目标可变为另类间方差尽可能的大

img = cv2.imread("../Question_01_10/imori.jpg")
img = img.astype(np.float32)
img_thre = img[:, :, 0] * 0.0722 + img[:, :, 1] * 0.7152 + img[:, :, 2] * 0.2126

max_l = -np.inf
best_t = 0
for i in range(255):
    class0 = img_thre[img_thre < i]
    class1 = img_thre[img_thre >= i]
    w0 = np.prod(class0.shape) / np.prod(img_thre.shape)
    w1 = np.prod(class1.shape) / np.prod(img_thre.shape)
    M0 = np.mean(class0)
    M1 = np.mean(class1)
    l = w0 * w1 * (M0 - M1)**2
    if l > max_l:
        max_l = l
        best_t = i
print(f"the best thresold is {best_t}")
img_thre[img_thre > best_t] = 255
img_thre[img_thre < best_t] = 0
cv2.imshow("thresholding image", img_thre)
cv2.waitKey(0)
cv2.destroyWindow("thresholding image")
