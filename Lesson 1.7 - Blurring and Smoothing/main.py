import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])

kernel_sizes = [(3, 3), (7, 7), (15, 15)]

for kernel_size in kernel_sizes:
    blurred = cv2.blur(image, kernel_size)
    cv2.imshow("Blue", blurred)
    cv2.waitKey(0)


cv2.destroyAllWindows()

for kernel_size in kernel_sizes:
    gaussian_blue = cv2.GaussianBlur(image, kernel_size, 0)
    cv2.imshow("Gaussian", gaussian_blue)
    cv2.waitKey(0)

cv2.destroyAllWindows()

for k in 3, 5, 7:
    median = cv2.medianBlur(image, k)
    cv2.imshow("Median blue", median)
    cv2.waitKey(0)

cv2.destroyAllWindows()

kernels = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for i in kernels:
    bilateral = cv2.bilateralFilter(image, i[0], i[1], i[2])
    cv2.imshow("Bilateral", bilateral)
    cv2.waitKey(0)