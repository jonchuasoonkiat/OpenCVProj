import cv2, time, pandas
from datetime import datetime

first_frame = None #create empty variable first

status_list = [None, None] #to check when object goes in frame and then leaves it. Addes two empty objects so python can find the second last object as well.
times=[]
df = pandas.DataFrame(columns = ["Start", "End"]) #create to store objects going in and out of frame

video = cv2.VideoCapture(0)

while True:
   
    check, frame = video.read()
    status=0
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
        status = 1

        (x, y, w, h) = cv2.boundingRect(contour) #creating  n rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3) # draw the rectangle in frame

    status_list.append(status) #recording the status from the loop that considers object moving in and out of frame
    #Recording the time given the conditionals of seqeuncing of object appearance as marked by 0 or 1
    if status_list[-1] == 1 and status_list[-2] == 0: 
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1: 
        times.append(datetime.now())
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)
    key=cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

#iterate through list and append to list
for i in range(0, len(times), 2):
    df=df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv") #export appended df to csv file.
video.release()
cv2.destroyAllWindows 