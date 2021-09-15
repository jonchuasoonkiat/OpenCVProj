import cv2
face_cascade =  cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#will search image for face and return the coordinates and size of face, and draw a rectangle for the face.
img=cv2.imread("photo.jpg")


gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert original image to grayscale

#create variable to store the height and width and coordinates of face
#what this does is to search for faces in different scales of the picture. Higher value = greater accuracy
#creates an array to store the detected box
faces = face_cascade.detectMultiScale(gray_img, 
scaleFactor=1.05,
minNeighbors=5)
#usually these two are the values used

for x, y, w, h in faces:
    img= cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)
    #(image name, top left corner, bottom right corner, color, width of line)

print(type(faces))
print(faces)

resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()