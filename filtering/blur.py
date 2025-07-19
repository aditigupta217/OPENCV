import cv2

image = cv2.imread("/Users/aditi/Desktop/opencv/filtering/Bible Verse Desktop Wallpapers.jpg")

blur = cv2.GaussianBlur(image,(7,7),0)

cv2.imshow("blurimage",blur)
cv2.imshow("orignal", image)
cv2.waitKey(0)
cv2.destroyAllWindows()