import numpy as np
import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

original_image = cv2.imread(args['image'])
(w, h) = original_image.shape[1], original_image.shape[0]
center_x, center_y = w // 2, h // 2

rotation_matrix = cv2.getRotationMatrix2D((center_x - 50, center_y - 50), 45, 0.5)
rotated_image = cv2.warpAffine(original_image, rotation_matrix, dsize=(w, h))

cv2.imshow("Rotation", rotated_image)
cv2.waitKey(0)


# and now using imutils
# original_image = cv2.imread(args["image"])
# rotated_image2 = imutils.rotate(original_image, 30)
# b, g, r = rotated_image2[254, 335]
# print(b, g, r)
#
# original_image = cv2.imread(args["image"])
# rotated_image2 = imutils.rotate(original_image, -110)
# b, g, r = rotated_image2[312, 136]
# print(b, g, r)
#
#
# cv2.waitKey(0)

original_image = cv2.imread(args["image"])
(h, w) = original_image.shape[:2]
center_x = w // 2
center_y = h // 2

rotation_matrix = cv2.getRotationMatrix2D((50, 50), 88, 1)
rotated_image = cv2.warpAffine(original_image, rotation_matrix, dsize=(w, h))
b, g, r = rotated_image[10, 10]
print(b, g, r)