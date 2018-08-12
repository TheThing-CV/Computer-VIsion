# cv2  - min-max 0 - 255 (clupping)
# numpy - wrap around

import numpy as np
import cv2
import argparse

print(cv2.add(np.uint8([255]), np.uint8([5])))
print(np.uint8([255]) + np.uint8([5]))

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

M = np.ones(image.shape, dtype='uint8') * 75
added = cv2.add(image, M)
cv2.imshow("CV2 addition", added)
b, g, r = added[152, 61]
print(r, g, b)

cv2.waitKey(0)

M = np.ones(image.shape, dtype='uint8') * 100
substract = cv2.subtract(image, M)
cv2.imshow("CV2 substract", substract)
cv2.waitKey(0)
