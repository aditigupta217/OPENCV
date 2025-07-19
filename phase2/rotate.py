import cv2

image = cv2.imread("/Users/aditi/Desktop/opencv/phase2/ChatGPT Image Mar 29, 2025 at 01_22_43 PM.png")

if image is None:
    print("Image not found")
else:
    print("Image load successfully")
    (h, w )= image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center,90,1.0)
    rotate = cv2.warpAffine(image, M, (w,h))
    cv2.imshow("orignal_image", image)
    cv2.imshow("resize_image", rotate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
