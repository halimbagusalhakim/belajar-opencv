import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

if ret:
    cv2.imwrite("my_photo.jpg", frame)
    cv2.waitKey(1000)
    gambar = cv2.imread("my_photo.jpg")
    cv2.imshow("gambar", gambar)
    cv2.waitKey(5000)
else:
    print("Can't save photo")

cap.release()


