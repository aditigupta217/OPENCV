import cv2

image = cv2.imread("/Users/aditi/Desktop/opencv/phase2/ChatGPT Image Mar 29, 2025 at 01_22_43 PM.png")

if image is None:
    print("Image not found")
else:
    print("Image load successfully")
    ptr1 = (50,100)
    ptr2 = (200,500)
    color = (255,0,0)
    thickness = 4
    line = cv2.line(image,ptr1,ptr2,color,thickness)
    cv2.imshow("line", line)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
