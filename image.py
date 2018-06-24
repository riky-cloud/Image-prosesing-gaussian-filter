import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gambar-noise.jpg')

blur = cv2.GaussianBlur(img,(5,5),0)

plt.subplot(121),plt.imshow(img),plt.title('Gambar Awal')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Setelah Di Proses')
plt.xticks([]), plt.yticks([])
plt.show()

# Riky Susanto
