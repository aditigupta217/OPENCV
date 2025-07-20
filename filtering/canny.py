import cv2

image = cv2.imread("/Users/aditi/Desktop/opencv/phase2/ChatGPT Image Mar 29, 2025 at 01_22_43 PM.png", cv2.IMREAD_GRAYSCALE)

edge = cv2.Canny(image,150,350)

cv2.imshow("orginal", image)
cv2.imshow("new",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
