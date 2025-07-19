import cv2

image = cv2.imread("/Users/aditi/Desktop/opencv/phase2/ChatGPT Image Mar 29, 2025 at 01_22_43 PM.png")

if image is None:
    print("Image not found")
else:
    print("Image load successfully")
   
    cv2.putText(image,"This is my cat, me and my saiyaara!!", (50,100),cv2.FONT_HERSHEY_COMPLEX, 1.2,(288,134,97),3)
    cv2.imshow("circle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    