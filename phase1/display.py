import cv2

image = cv2.imread("/Users/aditi/Desktop/opencv/phase1/ChatGPT Image Mar 28, 2025 at 10_58_32 PM.png")

if image is None:
    print("Error")
else:
    print("Image loaded successfully")
    cv2.imshow("Image showing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
