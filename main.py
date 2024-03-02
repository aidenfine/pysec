import cv2 
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error")
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation = cv2.INTER_AREA)
    cv2.imshow("input", frame)
    c = cv2.waitKey(1)

    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()