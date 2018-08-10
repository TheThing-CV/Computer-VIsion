import imutils
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
# cv2.imshow("Original", image)
# cv2.waitKey(0)
#
# aspect_ratio = 150 / image.shape[1]  # new width will be 150 pixels
# dim = (150, int(image.shape[0] * aspect_ratio))
# resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
#
# cv2.imshow("Resized", resized_image)
# cv2.waitKey(0)
#
# # and now aspect ration according to the height
#
# aspect_ratio = 100 / image.shape[0]  # new height / old height
# dim = (int(image.shape[1] * aspect_ratio), 100)
# resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
# cv2.imshow("Resized", resized_image)
# cv2.waitKey(0)
#
# new_image = imutils.resize(image, width=800)
# cv2.imshow("Resized", new_image)
# cv2.waitKey(0)
#
# methods = [("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
#            ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
#            ("cv2.INTER_AREA", cv2.INTER_AREA),
#            ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
#            ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
#
# for name, method in methods:
#     resized = imutils.resize(image, width=image.shape[0] * 3, inter=method)
#     cv2.imshow("Method: {}".format(name), resized)
#     cv2.waitKey(0)

image = cv2.imread(args['image'])
resized = cv2.resize(image, None, fx=2, fy=2)
b, g, r = resized[367, 170]
print(b, g, r)

