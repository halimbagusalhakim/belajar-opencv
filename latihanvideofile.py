#langkah langkah
##1. import cv2
##2. buat variabel yang berisi lokasi video
##3. buat variabel video untuk membaca lokasi file video
##4. buat pengkondisian jika video tidak terbuka maka menuliskan error
##5. membuat looping while video terbuka
##6. membaca data video
##7. pemngkondisian lagi jika data video terbaca akan menampilkan video
##8.menampilkan video 
import cv2 ##1. import cv2


lokasifilevideo = "assets\Video.mp4" ##2. buat variabel yang berisi lokasi video


video = cv2.VideoCapture(lokasifilevideo) ##3. buat variabel video untuk membaca lokasi file video


print(type(video))

if(video.isOpened()== False ): ##4. buat pengkondisian jika video tidak terbuka maka menuliskan error
    print("error")

while (video.isOpened()):##5. membuat looping while video terbuka
    ret, frame = video.read()##6. membaca data video
    if ret == True:##7. pemngkondisian lagi jika data video terbaca akan menampilkan video
        cv2.imshow('frame', frame)##8.menampilkan video 
        if cv2.waitKey(25) & 0xFF == ord('q'):##mebuat pengkondisian unutk menghentikan
            break
    else:
        break
video.release()#close video

cv2.destroyAllWindows()