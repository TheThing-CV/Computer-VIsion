import numpy as np
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
B, G, R = cv2.split(image)

final_image = cv2.merge([B, G, R])
print(R[94, 180])
print(B[78, 13])
print(G[5, 80])

cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)
cv2.imshow("Composite", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()