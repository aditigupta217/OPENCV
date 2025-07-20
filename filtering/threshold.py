import cv2

image = cv2.imread("/Users/aditi/Desktop/opencv/phase2/ChatGPT Image Mar 29, 2025 at 01_22_43 PM.png",cv2.IMREAD_GRAYSCALE)

ret, threshold = cv2.threshold(image,120,50,cv2.THRESH_BINARY)
 
cv2.imshow("image",image)
cv2.imshow("threshold image", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()