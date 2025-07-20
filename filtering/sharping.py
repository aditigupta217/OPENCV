import cv2
import numpy as np

image = cv2.imread("/Users/aditi/Desktop/opencv/filtering/Bible Verse Desktop Wallpapers.jpg")

sharp_ker = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

sharpening = cv2.filter2D(image,-1,sharp_ker)

cv2.imshow("orignal", image)
cv2.imshow("sharpen",sharpening)
cv2.waitKey(0)
cv2.destroyAllWindows()



