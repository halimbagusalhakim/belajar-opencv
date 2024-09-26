

import cv2

LokasiFileFoto = "assets\Lucu.jpeg"

Foto = cv2.imread(LokasiFileFoto)
cv2.imshow("ini foto", Foto)
cv2.waitKey(1000)
print(Foto[1023,820]) #menampilkan data GBR pada (-y,x), ini diubah sesuai ukuran foto


cv2.destroyAllWindows()
