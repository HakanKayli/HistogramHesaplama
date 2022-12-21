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



h = 300
w = 400

original = cv2.imread("kaptanamerika.jpeg",0)
original = cv2.resize(original,(w,h))

image = cv2.imread("kaptanamerika.jpeg",0)
image = cv2.resize(image,(w,h))

[h,w] = shape(image)
image2 = zeros([h,w], dtype=np.uint8)

max = 0

#maximumu bulma döngüsü
for i in range (h):
    for j in range (w):
        if max < image [i,j]:
            max = image [i,j]


#maximumdan görüntü matrisinin her değerini çıkarma döngüsü
for i in range (h):
    for j in range (w):
        image2[i,j] = max - image[i,j]


cv2.imshow("original", original)
cv2.imshow("gri",image)
cv2.imshow("ters cevrilmis",image2)
cv2.waitKey()
