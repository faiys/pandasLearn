import cv2
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("cannot open")
    exit()
while True:
    success, frame = cap.read()
    if success:
        cv2.imshow("open CV", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()