import cv2

image = cv2.imread('florida_trip.png')
cv2.imshow("De", image)
cv2.waitKey(0)

# now take ROI - region of interest

roi = image[90:450, 0:290]  # y goes first, x - second
cv2.imshow("ROI", roi)
cv2.waitKey(0)