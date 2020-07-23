# 二值化, 阀值设定为128
import cv2

img = cv2.imread("../Question_01_10/imori.jpg")
img_thre = img[:, :, 0] * 0.0722 + img[:, :, 1] * 0.7152 + img[:, :, 2] * 0.2126
img_thre = img_thre.astype("uint8")
img_thre[img_thre>128] = 255
img_thre[img_thre<128] = 0
cv2.imshow("thresholding image",img_thre)
cv2.waitKey(0)
cv2.destroyWindow("thresholding image")