import cv2

# Reading the video
vidcap = cv2.VideoCapture('capture.mp4')
success, image = vidcap.read()
print(success)
count = 0
success = True
idx = 0

print(success)

# Read the video frame by frame
while success:
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("lelel", hsv)

    success, image = vidcap.read()


