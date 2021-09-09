import cv2

cap = cv2.VideoCapture("resources/DAZN_vs_2019_J1_33-ykSvZi0z2tI.mp4")

while True:
  success, img = cap.read()
  cv2.imshow("Video", img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  