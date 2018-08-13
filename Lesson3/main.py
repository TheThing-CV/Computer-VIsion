import numpy as np
import cv2
import random


canvas = np.zeros((450, 450, 3), dtype='uint8')
cv2.line(canvas, (0, 0), (450, 450), (0, 255, 0), thickness=4)
cv2.imshow("Thick line", canvas)
cv2.waitKey(0)

# create new canvas
canvas2 = np.zeros((450, 450, 3), dtype='uint8')

for i in range(10):
    start_Y = random.randint(0, 450)
    start_X = random.randint(0, 450)
    end_Y = random.randint(0, 450)
    end_X = random.randint(0, 450)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    thickness = random.randint(1, 6)
    cv2.line(canvas2, (start_Y, start_X), (end_Y, end_X), color, thickness=thickness)
    cv2.imshow("Random lines", canvas2)

cv2.waitKey(0)

cv2.rectangle(canvas2, (0, 0), (20, 40), (255, 127, 0), thickness=-1)
cv2.imshow("Rectangle", canvas2)
cv2.waitKey(0)

new_canvas = np.zeros((500, 500, 3), dtype='uint8')
(center_X, center_Y) = new_canvas.shape[1] // 2, new_canvas.shape[0] // 2

for r in range(0, 175, 25):
    cv2.circle(new_canvas, (center_X, center_Y), r, color=(r, r, r))

cv2.imshow("Circles", new_canvas)
cv2.waitKey(0)

new_canvas2 = np.zeros((500, 500, 3), dtype='uint8')


for i in range(25):
    color = np.random.randint(0, 255, size=(3, )).tolist()
    center = np.random.randint(0, 500, size=(2, ))
    radius = np.random.randint(1, 200)
    cv2.circle(new_canvas2, tuple(center), radius, color, thickness=-1)
    cv2.imshow("Figures", new_canvas2)

cv2.waitKey(0)
