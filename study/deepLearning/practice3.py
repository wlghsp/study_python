import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('lenna.png')

plt.imshow(img)
plt.show()
