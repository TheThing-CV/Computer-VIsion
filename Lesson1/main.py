import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to image')
ap.add_argument('-o', '--output', required=False, help='Output name')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
print(f'Image width = {image.shape[1]}')
print(f'Image height = {image.shape[0]}')
print(f'Image channels = {image.shape[2]}')

cv2.imshow("Windows", image)
cv2.imwrite(args['output'], image)

cv2.waitKey(0)

