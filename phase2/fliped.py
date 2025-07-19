import cv2

image = cv2.imread("/Users/aditi/Desktop/opencv/phase2/ChatGPT Image Mar 29, 2025 at 01_22_43 PM.png")

if image is None:
    print("Image not found")
else:
    print("Image load successfully")
    flip_hor = cv2.flip(image,1)
    flip_ver = cv2.flip(image,0)
    flip_both = cv2.flip(image,-1)
    cv2.imshow("orignal_image", image)
    cv2.imshow("horizontal",flip_hor)
    cv2.imshow("both",flip_both)
    cv2.imshow("vertical",flip_ver)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
