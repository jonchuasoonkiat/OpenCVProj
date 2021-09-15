import cv2

#second argument is how you want to read your image. 1 = RGB, 0 = grayscale, -1 = colour with transparency 
img = cv2.imread("galaxy.jpg", 0)

#image type = numpy.ndarray
#print(type(img))
#find out how many pixels are in the image
#print(img.shape)
#check dimension of your arrays
#print(img.ndim)

#resized_image=cv2.resize(img, (1000,1000))
resized_image=cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2))) #using proportion to resize instead.
cv2.imshow("Galaxy", resized_image)

#writing new image in new file
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0) #in milliseconds. If 0, then waits for any key.
cv2.destroyAllWindows() #method that closes windows

