import cv2
import numpy as np

img_file = "resources/women-2763219_960_720.png"
img_file2 = "resources/woman-1274056_960_720.jpg"

# cap = cv2.VideoCapture("resources/DAZN_vs_2019_J1_33-ykSvZi0z2tI.mp4")
# cap = cv2.VideoCapture(1)

# window
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(10, 100)

# while True:
#   success, img = cap.read()
#   cv2.imshow("Video", img)
#   if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

img = cv2.imread(img_file2)
karnel = np.ones((5, 5), np.uint8)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
# エッジを得る　（数値：閾値）
img_canny = cv2.Canny(img, 100, 100)
# 閾値差異確認（エッジが確認しやすい）
img_canny2 = cv2.Canny(img, 150, 200)
img_dialation = cv2.dilate(img_canny2, karnel, iterations=1)
img_eroded = cv2.erode(img_dialation, karnel, iterations=1)

# cv2.imshow("Gray Image", img_gray)
# cv2.imshow("Blur Image", img_blur)
# cv2.imshow("Canny Image", img_canny)
cv2.imshow("Canny2 Image", img_canny2)
cv2.imshow("Dialation Image", img_dialation)
cv2.imshow("Eroded Image", img_eroded)

cv2.waitKey(0)