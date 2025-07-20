import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, fram = cap.read()
    if not ret :
        print("Could not find ")
        break

    cv2.imshow("webcam Fedd", fram)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Qutiingg')
        break

cap.release()
cv2.destroyAllWindows()

