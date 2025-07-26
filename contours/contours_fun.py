import cv2

img = cv2.imread("/Users/aditi/Desktop/opencv/contours/yellow-triangle-geometric-shape-vector_53876-175072.jpg.avif")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray,220,240,cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,255,0), 3)

for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    coners = len(approx)
    if coners == 3:
        shapename = 'triangle'
    elif coners == 4:
        shapename = "rectangle"
    elif coners == 5:
        shapename = "circle"
    else:
        shapename = "unshaped"
        
    cv2. drawContours(img,[approx], 0, (0,255,0), 2)

    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10

    cv2.putText(img,shapename,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,255),2)


cv2.imshow("Contours", img)
cv2.waitKey (0)
cv2.destroyAllWindows( )