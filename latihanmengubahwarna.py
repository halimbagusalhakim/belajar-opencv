import cv2

lokasifilefoto = "assets\download (2).png"

foto = cv2.imread(lokasifilefoto)

cv2.imshow("foto awal", foto)

warnadirubah = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
cv2.imshow("setelah dirubah", warnadirubah)

cv2.waitKey()
cv2.destroyAllWindows()
