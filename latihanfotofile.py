#langkah langkah
##1. import cv2
##2. buat variabel unutuk lokasi fotonya
##3. buat variabel unutk memmbaca dari lokasi fotonya
##4.menampilkan foto
##

import cv2 ##1. import cv2

lokasifilefoto = "assets\download (2).png" ##2. buat variabel unutuk lokasi fotonya


foto =cv2.imread(lokasifilefoto) ##3. buat variabel unutk memmbaca dari lokasi fotonya

cv2.imshow("ini foto", foto) ##4.menampilkan foto

cv2.waitKey(1000)

cv2.destroyAllWindows()