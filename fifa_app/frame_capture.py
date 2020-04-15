import cv2

# Opens the Video file
cap = cv2.VideoCapture('capture.mp4')
i = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False or i>1500:
        break
    if i>700 and i%5==0:
        cv2.imwrite('frames/fifa' + str(i) + '.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()