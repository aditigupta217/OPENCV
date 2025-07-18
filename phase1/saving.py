import cv2

image = cv2.imread("/Users/aditi/Desktop/opencv/phase1/ChatGPT Image Mar 28, 2025 at 10_58_32 PM.png")

if image is not None:
    sucess = cv2.imwrite("new_name.png", image)
    if sucess:
        print("Image save sucessfully as 'new_name.png' ")
    else:
        print("Fail to save ")
else:
    print("Error : image could not found")