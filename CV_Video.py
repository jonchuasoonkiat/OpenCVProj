import cv2, time
video = cv2.VideoCapture(0)
a=1

while True:
   
    a=a+1 #to check for how many frames have been captured
   
    check, frame = video.read()
    print(check) #check if the video is running
    print(frame)

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    #hold the script for 3 seconds
    #time.sleep(3)

    cv2.imshow("Capturing", gray)

    key=cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows 