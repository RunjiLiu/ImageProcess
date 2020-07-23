# 灰度化
import cv2

img = cv2.imread("../Question_01_10/imori.jpg")
img_gray = img[:, :, 0] * 0.0722 + img[:, :, 1] * 0.7152 + img[:, :, 2] * 0.2126
img_gray = img_gray.astype("uint8")  # 这一步很重要，如果是浮点数会显示空白
cv2.imshow("gray image", img_gray)
cv2.imshow("origin image", img)
cv2.waitKey(0)
