import cv2, time
first_frame = None #create empty variable first
video = cv2.VideoCapture(0)

while True:
   
    check, frame = video.read()
    print(check) #check if the video is running
    print(frame)

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray, (21, 21), 0) #we want to make it blurry to reduce noise and increase accuracy when calculating difference. Arguments = evel of blur, standard deviation.

    if first_frame is None:
        first_frame = gray
        continue
    
    #finding the difference
    delta_frame = cv2.absdiff(first_frame, gray)

    #setting a threshold 
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    #smoothing out the whites in the threshold frames
    thresh_frame = cv2.dilate(thresh_delta, None, iterations= 2)

    #find contours of the distinct objects in the frame and store them 
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #fitler out the unwanted contours

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour) #creating  n rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3) # draw the rectangle in frame

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)
    key=cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows 