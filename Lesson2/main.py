import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
(h, w) = image.shape[:2]

cv2.imshow("Lesson 2", image)

(b, g, r) = image[225, 111]
print(f'Pixel at [0, 0] is R: {r}, G: {g}, B: {b}')

# change the value

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print('Changing some values....')
print(f'Pixel at [0, 0] is R: {r}, G: {g}, B: {b}')

(center_x, center_y) = w // 2, h // 2

top_left = image[0:center_y, 0:center_x]
top_right = image[0:center_y, center_x:w]
bottom_left = image[center_y:h, 0:center_x]
bottom_right = image[center_y:h, center_x:w]

cv2.imshow("tl", top_left)
cv2.imshow("tr", top_right)
cv2.imshow("bl", bottom_left)
cv2.imshow("br", bottom_right)

image[0:center_y, 0:w] = (255, 0, 0)
cv2.imshow("Filled up", image)

cv2.waitKey(0)
