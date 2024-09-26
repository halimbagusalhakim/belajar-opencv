import cv2


lokasifilefoto = "assets\download (2).png"

Foto = cv2.imread(lokasifilefoto)

cv2.imshow("ini foto" , Foto)

DataShape = Foto.shape

s1 = Foto.shape[0]
s2 = Foto.shape[1]
s3 = Foto.shape[2]

print(Foto.size)
print(DataShape)
print(s1)
print(s2)
print(s3)

cv2.waitKey(2000)
FotoResize = cv2.resize(Foto, (1000,500)) #mengganti ukuran (lebar dan tinggi)
cv2.imshow("ini foto setelah resize", FotoResize)
print(FotoResize.shape)

cv2.waitKey()
cv2.destroyAllWindows()
