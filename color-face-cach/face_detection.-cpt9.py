import cv2

img_path = "resources/DSCN2730.JPG"
img_path2 = "resources/woman-1274056_960_720.jpg"

faceCascade = cv2.CascadeClassifier(
    "resources/haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread(img_path)
img = cv2.resize(img,(1000,800))


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
