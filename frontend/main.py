import numpy as np
print('start')
import cv2

# Load an color image in grayscale
img = cv2.imread('200.jpg',1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

