import cv2

face_cascade = cv2.CascadeClassifier("/Users/aditi/Desktop/opencv/face_and_object/haarcascade_frontalface_default.xml")
face_eye = cv2.CascadeClassifier("/Users/aditi/Desktop/opencv/face_and_object/haarcascade_eye.xml")
face_smile = cv2.CascadeClassifier("/Users/aditi/Desktop/opencv/face_and_object/haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y), (x+w, y+h), (0,255,0), 2)

        roi_gray = gray[y:y+h , x:x+w]
        roi_color = frame[y:y+h , x:x+w]

        eyes = face_eye.detectMultiScale(roi_gray,1.1,10)
        if len(eyes)>0:
            cv2.putText(frame, "Eyes Detected", (x, y-30), cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,255),2)
    
        smile = face_smile.detectMultiScale(roi_gray,1.7,20)
        if len(smile)>0:
            cv2.putText(frame, "smile Detected", (x, y-50), cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,255),2)

    cv2.imshow("Smart face detecter", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
