# BGR -> RGB
import cv2

img = cv2.imread("../Question_01_10/imori.jpg")  # BGR通道
img2 = img[:, :, [2, 1, 0]].copy()
cv2.imshow("BGR", img)
cv2.imshow("RGB", img2)
cv2.waitKey(100)
