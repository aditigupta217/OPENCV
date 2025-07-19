import cv2

image = cv2.imread("/Users/aditi/Desktop/opencv/phase2/ChatGPT Image Mar 29, 2025 at 01_22_43 PM.png")

if image is None:
    print("Image not found")
else:
    print("Image load successfully")
    crop = image[100:600,200:800]
    cv2.imshow("orignal_image", image)
    cv2.imshow("resize_image",crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()