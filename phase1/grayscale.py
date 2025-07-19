import cv2

image = cv2.imread("/Users/aditi/Desktop/opencv/phase1/ChatGPT Image Mar 28, 2025 at 10_58_32 PM.png")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray_picture" , gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("Gray_newpic.png", gray )
else:
    print("Colud Not find ")