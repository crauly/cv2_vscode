import cv2, numpy as np
from cv2_self_functions import stackImages, getContours

file = "resources/For_figure_detection.png"
img = cv2.imread(file)

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)

img_stack = stackImages(0.6, ([img, img_gray, img_blur])

# cv2.imshow("Original", img)
# cv2.imshow("Gray Image", img_gray)
# cv2.imshow("Blur Image", img_blur)
cv2.imshow("Stack Image", img_stack)

cv2.waitKey(0)

