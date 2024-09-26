#langkah langkah
##1. import cv
##2. membuat variabel kamera untuk mengecek ketersediaan kamera
##3. mengset ukuran video kamera
##4. membuat looping while jika kamera terbuka
##5. membaca data kamera
##6. menampilkan video dari kamera
##7. mengubah warna dari video kamera
##8. menampilkan video dari kamera setelah diubah warnanya


import cv2##1. import cv


kamera = cv2.VideoCapture(0)##2. membuat variabel kamera untuk mengecek ketersediaan kamera

##3. mengset ukuran video kamera
panjang = 1280
lebar = 720
kamera.set(3, panjang)
kamera.set(4, lebar)

print(kamera.isOpened())

while(kamera.isOpened()):##4. membuat looping while jika kamera terbuka
    _, frame = kamera.read()##5. membaca data kamera
    cv2.imshow("frame kamera", frame)##6. menampilkan video dari kamera
    videodirubah = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)##7. mengubah warna dari video kamera
    cv2.imshow("video setelah dirubah ", videodirubah)##8. menampilkan video dari kamera setelah diubah warnanya

    key = cv2.waitKey(1)
    if  key == ord('q'):
        break

cv2.destroyAllWindows()