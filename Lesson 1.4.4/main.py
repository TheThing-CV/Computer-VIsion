import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Path to file")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
flipped = cv2.flip(image, 1)
rotated = imutils.rotate(flipped, 45)
flipped = cv2.flip(rotated, 0)

cv2.imshow("Fliped", flipped)

b, g, r = flipped[189, 441]
print(b, g, r)
cv2.waitKey(0)