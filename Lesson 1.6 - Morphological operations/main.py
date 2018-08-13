import numpy as np
import cv2
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for i in range(3):
    eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Eroded {} times".format(i + 1), eroded)
    if i == 2:
        cv2.imwrite('eroded.png', eroded)
    cv2.waitKey(0)

cv2.destroyAllWindows()

for i in range(3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Dilated {} times".format(i + 1), dilated)
    if i == 2:
        cv2.imwrite('dilation.png', dilated)
    cv2.waitKey(0)

cv2.destroyAllWindows()

kernel_sizes = [(3, 3), (5, 5), (7, 7)]

for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening", opening)
    cv2.waitKey(0)

cv2.destroyAllWindows()

for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing", closing)
    cv2.waitKey(0)