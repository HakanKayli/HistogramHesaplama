import cv2
from matplotlib import pyplot as plt
from numpy import zeros, shape


foto = cv2.imread("kaptanamerika.jpeg",0)

Hist = zeros(256)
[w,h] = shape(foto)

for i in range (0,w):
    for j in range (0,h):
        a = foto[i,j]
        Hist[a] = Hist[a] + 1

plt.plot(Hist)
plt.show()

cv2.imshow("Kaptan Amerika", foto)
cv2.waitKey()
