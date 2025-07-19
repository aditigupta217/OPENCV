import cv2

image = cv2.imread("/Users/aditi/Desktop/opencv/phase2/ChatGPT Image Mar 29, 2025 at 01_22_43 PM.png")

if image is None:
    print("Image not found")
else:
    print("Image load successfully")
   
    color = (255,0,0)
   
    cv2.circle(image,(350,350),80,color,5)
    cv2.imshow("circle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
