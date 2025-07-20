import cv2

image = cv2.imread("/Users/aditi/Desktop/opencv/filtering/Bible Verse Desktop Wallpapers.jpg")

blurred = cv2.medianBlur(image,11)
cv2.imshow("orignal",image)
cv2.imshow("clean", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

