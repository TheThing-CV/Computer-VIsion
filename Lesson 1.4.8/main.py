import numpy as np
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])

mask = np.zeros(image.shape[:2], dtype='uint8')
mask = cv2.circle(mask, (250, 250), 150, 255, -1)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Mask", result)
cv2.waitKey(0)