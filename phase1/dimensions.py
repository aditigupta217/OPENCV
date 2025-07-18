import cv2

image = cv2.imread("/Users/aditi/Desktop/opencv/phase1/ChatGPT Image Mar 28, 2025 at 10_58_32 PM.png")

if image is not None:
    h, w, c = image.shape
    print(f"Image load succesfully :\nheight {h} , \nwidth {w} , \nchannel {c}")
else:
    print("The image not found !!")