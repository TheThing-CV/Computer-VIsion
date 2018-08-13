import numpy as np
import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

translate_matrix = np.float32([[1, 0, 25], [0, 1, 100]])  # right and down 100
# load image

image = cv2.imread(args['image'])
shifted_image = cv2.warpAffine(image, translate_matrix, dsize=(image.shape[1], image.shape[0]))
cv2.imshow("Translated", shifted_image)
cv2.waitKey(0)

# this time we'll use imutils package

image = cv2.imread(args['image'])
shifted_image = imutils.translate(image, -100, -100)
cv2.imshow("Imutils", shifted_image)
cv2.waitKey(0)
