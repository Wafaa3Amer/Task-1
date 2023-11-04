import cv2
#ret is a boolean variable that returns true if the frame is available
#rame is an image array vector captured based on the default frames per second defined explicitly or implicitly
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imshow('Camera', frame)
cv2.imwrite('captured_photo.png', frame)
print("Photo saved as 'captured_photo.png'")
cv2.waitKey(0)
cv2.destroyAllWindows()
